import hjson

from rich.console import Console

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
    self.theme_templates_dir = self.theme_dir / "templates"
    self.theme_assets_dir = self.theme_dir / "assets"

  def no_access(self, error):
    econsole.print(f'Can not access: {error.filename}')

  def build(self):
    for root, dirs, files in self.content_dir.walk(on_error=self.no_access):
      for file in files:
        print(file)
