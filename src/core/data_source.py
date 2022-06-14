from src.config.config import WeekDates
from src.core.models import Student, Lesson
from src.services.database import Database


class LocalDataSource:
  """
  Local data source implementation.
  Performs requests to database and formats
  received data into json-like objects
  """

  factors = None
  database = None
  week = None

  def __init__(self, factors: tuple, week: WeekDates, db: Database) -> None:
    """ Constructor """
    self.factors = factors
    self.database = db
    self.week = week

  def __convert_result(self, data: list[tuple]) -> dict:
    """ Convert the given students list into a dict """
    students = {}

    for student in data:
      _id, name = student[0], student[1]
      lesson = Lesson(values={
        key: value for key, value in zip(self.factors, student[2:])
      })

      if students.get(name) is None:
        students.update({name: Student(_id, name, [lesson])})
      else:
        students[name].lessons.append(lesson)

    return students

  def get_students_by(self, ids: tuple = None, names: tuple = None) -> dict:
    """ Get students by given list of ids or names """
    students_data = self.database.get_students_by(
      *self.week.values,
      ids=ids, names=names,
      factors=self.factors)

    return self.__convert_result(students_data)

  def get_students_by_week(self) -> dict:
    """ Get all students with classes on given week """
    students_data = self.database.get_students_by_week(
      *self.week.values,
      factors=self.factors)

    return self.__convert_result(students_data)
