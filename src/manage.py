import sys

from src.boot.interface import run_interface
from src.boot.script import run_script


def manage() -> None:
  """ Run interface or script itself according to { -interface } flag """
  if '-interface' in sys.argv[1:]:
    run_interface()
  else:
    run_script(sys.argv[1:])


if __name__ == '__main__':
  manage()
