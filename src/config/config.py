from pathlib import Path

from src.core.structures import WeekDates
from src.services.database import Database
from src.utils.utils import Utils


class Configuration:
  """ Class contains all configuration for script """

  BASE_DIR = Path(__file__).resolve().parent.parent  # Project root directory

  DB_FILE_NAME = 'database.db'  # Database file name

  EXCEL_FILE_NAME = 'total_scores.xlsx'  # Excel file name

  DB_PATH = BASE_DIR / DB_FILE_NAME  # Database file complete path

  EXCEL_PATH = BASE_DIR / EXCEL_FILE_NAME  # Excel file complete path

  """
  This factors will be used in calculations
  !IMPORTANT:
    values HAVE TO have the same name as table column names!
    If you added a new column into table, for example: 
    added column new_param into ClassesData (Таблица 4.), 
    then to use it inside script add 'new_param' into FACTORS!
    To use it in further calculations the only thing you need to do is
    create calculation methods in `core.models.Lesson` class
    NOTE: method must have a __calculate_{new_param} name! 
    and use received value as `self.new_param`!.
    Better to read in readme.md file.
  """
  FACTORS = ('activity', 'homework', 'test')

  week_dates = None  # Week dates interval [start, end]

  database = None  # Database instance

  names = None
  ids = None

  def __init__(self, arguments: list, ids: tuple = None,
               names: tuple = None) -> None:
    """ Constructor. Arguments parsing and database initialization """
    try:
      args = Utils.parse_cmd_args(arguments)
      self.database = Database(self.DB_PATH)
      self.week_dates = WeekDates(*Utils.date_to_week(args['start_date']))
      self.ids = tuple(ids) if ids else args['ids']
      self.names = tuple(names) if names else args['names']
    except ValueError:
      raise Exception(
        '[Configuration]: Invalid parameters provided! '
        'Check the -from=, -ids= or -names= param!')
    except Database.exception:
      raise Exception(
        '[Configuration]: Failed to open database! Check DB_PATH variable!')
    except TypeError:
      print('[Configuration]: Running from interface. No dates provided!')
    else:
      print('[Configuration]: Initialized with dates:', self.week_dates.values)
