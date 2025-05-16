from copy import deepcopy
from pathlib import Path

from django.template import Context, Template, engines
from django.conf import settings

import frontmatter
import hjson
import markdown2
from rich.console import Console

from pubcrank.lib.frontmatter import HJSONHandler

econsole = Console(stderr=True, style="bold red")
console = Console()


class Crank:
  def __init__(self, config):
    with config.open('r') as fh:
      self.config = hjson.loads(fh.read())

    self.dir = config.parent

    self.content_dir = self.dir / "content"
    self.templates_dir = self.dir / "templates"
    self.assets_dir = self.dir / "assets"

    self.theme_dir = self.dir / "themes" / self.config["theme"]
    self.theme_assets_dir = self.theme_dir / "assets"

    self.content_cache = {}
    self.tpl_cache = {}
    self.tpl_engine = None
    for e in engines.all():
      if e.name == 'pubcrank':
        self.tpl_engine = e.engine

  def no_access(self, error):
    econsole.print(f'Can not access: {error.filename}')

  def log(self, message, verbose=False):
    if verbose:
      console.print(message)

  def success(self, message):
    console.print(message, style="green")

  def build(self, outdir, verbose=False):
    for root, dirs, files in self.content_dir.walk(on_error=self.no_access):
      for f in files:
        file = root / f
        if file.suffix.lower() == '.md':
          relpath = file.relative_to(self.content_dir)
          outpath = outdir / relpath
          outpath = outpath.with_suffix('.html')
          self.log(f"Building: {file} -> {outpath}", verbose)
          self.generate(file, outpath)

    self.success(f"Successful build at: {outdir.resolve()}")

  def get_template(self, tpl_file):
    if tpl_file not in self.tpl_cache:
      tpl_path = self.templates_dir / tpl_file
      if not tpl_path.exists():
        tpl_path = self.theme_dir / tpl_file

      with tpl_path.open('r') as fh:
        self.tpl_cache[tpl_file] = Template(fh.read(), engine=self.tpl_engine)

    return self.tpl_cache[tpl_file]

  def open_content(self, file):
    key = file.resolve()
    if key in self.content_cache:
      return self.content_cache[key]

    with file.open('r') as fh:
      metadata, content = frontmatter.parse(fh.read(), handler=HJSONHandler())

    self.content_cache[key] = (metadata, content)
    return self.content_cache[key]

  def generate(self, src, dest):
    metadata, content = self.open_content(src)

    template = self.get_template(metadata.get('template', 'page.html'))
    context = deepcopy(self.config)
    context['src'] = src
    context['dest'] = dest
    context['crank'] = self

    page = metadata
    content = markdown2.markdown(content, extras=settings.PUBCRANK_MD_EXTRAS)
    page.update({'body': content})
    context.update({'page': page})
    context = Context(context)
    html = template.render(context)

    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open('w') as fh:
      fh.write(html)
