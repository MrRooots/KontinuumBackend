from src.config.config import Configuration
from src.core.repository import Repository
from src.utils.utils import Utils
from src.services.interface import Interface


def main(config: Configuration, repository: Repository,
         ids: tuple = None, names: tuple = None) -> None:
  """
  Compute total score for all student per given week.
  OR
  If `students_params` is not `Null` then compute total score
  for selected student per given week.
  Build excel file and open it. Opening tested only on WIN.
  """
  if ids:
    students = repository.get_students_by(ids=ids)
  elif names:
    students = repository.get_students_by(names=names)
  else:
    students = repository.get_students_by_week()

  for _, student in students.items():
    print(student, student.total_points)

  if students:
    Utils.open_as_excel(
      config.EXCEL_PATH,
      *zip(*((student.name, student.total_points)
             for _, student in students.items())),
      config.week_dates
    )
  else:
    Interface.show_popup()
    print('There ane no any records for given dates!')
