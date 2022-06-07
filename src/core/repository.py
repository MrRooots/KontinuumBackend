from src.config.config import WeekDates, Configuration
from src.core.data_source import LocalDataSource


class Repository:
  """ Main data repository """

  def __init__(self, cfg: Configuration, ds: LocalDataSource) -> None:
    """ Constructor """
    self.config = cfg
    self.data_source = ds

  def get_students_by(self, ids: tuple = None, names: tuple = None) -> dict:
    """ Get students by given tuple of ids or names """
    return self.data_source.get_students_by(ids, names)

  def get_students_by_week(self) -> dict:
    """ Get all students with lessons on given week """
    return self.data_source.get_students_by_week()
