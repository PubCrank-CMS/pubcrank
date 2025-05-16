from pathlib import Path

from django import template

import frontmatter


register = template.Library()

@register.simple_tag(takes_context=True)
def list_pages(context, dirpath, recursive=True):
  if not isinstance(dirpath, Path):
    if dirpath.startswith('.'):
      dirpath = context['src'].parent.joinpath(dirpath)

    else:
      dirpath = Path(dirpath)

  to_process = []
  if recursive:
    for root, dirs, files in dirpath.walk(on_error=context['crank'].no_access):
      for f in files:
        file = root / f
        if f.lower() != 'index.md' and file.suffix.lower() == '.md':
          metadata, content = context['crank'].open_content(file)
          to_process.append((file, metadata))

  else:
    for file in dirpath.iterdir():
      if file.name.lower() != 'index.md' and file.is_file() and file.suffix.lower() == '.md':
        metadata, content = context['crank'].open_content(file)
        to_process.append((file, metadata))

  print(to_process)
  return 'NARF'
