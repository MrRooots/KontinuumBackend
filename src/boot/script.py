from src.boot.main import main
from src.config.config import Configuration
from src.core.data_source import LocalDataSource
from src.core.repository import Repository


def run_script(args: list, ids: list = None, names: list = None) -> None:
  """ Run script """
  config = Configuration(args, ids=ids, names=names)
  local_data_source = LocalDataSource(config.FACTORS, config.week_dates,
                                      config.database)
  repository = Repository(config, local_data_source)

  main(config, repository, ids=config.ids, names=config.names)