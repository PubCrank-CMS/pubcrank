#!/usr/bin/env python3

import sys

import hjson
import frontmatter

from pubcrank.lib.frontmatter import HJSONHandler

def run(*files):
  for f in files:
    print(f)
    with open(f, 'r') as fh:
      meta, content = frontmatter.parse(fh.read())

    post = frontmatter.Post(content, handler=HJSONHandler(), **meta)
    with open(f, 'w') as fh:
      fh.write(frontmatter.dumps(post, handler=HJSONHandler()))
      fh.write("\n")

if __name__ == '__main__':
  run(*sys.argv[1:])
