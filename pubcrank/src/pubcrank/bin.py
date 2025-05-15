from pathlib import Path
import sys

from piou import Cli, Option
from rich.console import Console

from pubcrank.crank import Crank

econsole = Console(stderr=True, style="bold red")
cli = Cli(description='Pubcrank static site generator')

ConfigOption = Option(Path("pubcrank.hjson"), "-c", "--config", help="Config file")

def eprint(message):
  econsole.print(f"Error: {message}")


@cli.command(help='build your site')
def build(
  config: Path = ConfigOption
):
  if not config.exists():
    eprint("Config file does not exist.")
    sys.exit(1)

  crank = Crank(config)
  crank.build()

if __name__ == '__main__':
  cli.run()
