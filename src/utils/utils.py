import datetime
import os

from pandas import DataFrame

from src.config.structures import WeekDates

INPUT_FMT = '%Y.%m.%d'
MAIN_FMT = '%Y-%m-%d'


class Utils:
  """ Simple utilities """

  @staticmethod
  def get_week(start: datetime.datetime) -> tuple:
    """ Subtract 6 days to given date """
    end = start + datetime.timedelta(days=-6)

    return end.strftime(MAIN_FMT), start.strftime(MAIN_FMT)

  @staticmethod
  def date_to_week(s: str) -> tuple:
    """ Convert list of string to list of dates """
    return Utils.get_week(datetime.datetime.strptime(s, INPUT_FMT))

  @staticmethod
  def clear_arg(arg: str) -> list[str]:
    """ Clear given argument string. Remove [] and ' '. Split by '=' sign """
    for pattern in (' ', '[', ']'):
      arg = arg.replace(pattern, '')
    return arg.split('=')

  @staticmethod
  def parse_cmd_args(args: list[str]) -> dict[str, str or None]:
    """ Parse CMD arguments """
    if '-interface' in args:
      return {'start_date': None}
    else:
      start_date = '2021.10.24'
      ids, names = None, None

      for arg in args:
        arg = Utils.clear_arg(arg)
        if '-from' in arg:
          start_date = arg[-1]
        elif '-names' in arg:
          names = tuple(i for i in arg[-1].split(','))
        elif '-ids' in arg:
          ids = tuple(int(i) for i in arg[-1].split(','))

      return {'start_date': start_date, 'ids': ids, 'names': names}

  @staticmethod
  def open_as_excel(path: str, names: tuple, points: tuple,
                    week: WeekDates) -> None:
    """ Combine given data to excel table and open it """
    df = DataFrame({'Students': names, 'Total Score': points})

    df.to_excel(path, sheet_name=' to '.join(week.values), index=False)

    os.system(f'start "excel" {path}')
