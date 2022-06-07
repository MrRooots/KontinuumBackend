from src.boot.script import run_script
from src.services.interface import Interface


def run_interface() -> None:
  """ Run interface -> collect data -> run script """
  dates, ids, names = Interface.run_with_interface()
  run_script([f'-from={dates}'], ids, names)