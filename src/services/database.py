import sqlite3

from src.services.db_query_builder import DBQuery


class Database:
  """ Database implementation """
  connection = None
  cursor = None
  exception = sqlite3.Error

  def __init__(self, path) -> None:
    """ Constructor """
    self.connection = sqlite3.connect(path)
    self.cursor = self.connection.cursor()
    print('[Database]: Connection initialized successfully!')

  def __del__(self) -> None:
    """ Close connection """
    self.cursor.close()
    self.connection.close()
    print('[Database]: Connection closed')

  def __make_request(self, query) -> list:
    """ Execute given SQL query """
    try:
      return self.cursor.execute(query).fetchall()
    except sqlite3.Error as error:
      print('[Database]: make_request failed with:', error)
      return []

  def get_students_by(self, start: str, end: str, ids: tuple,
                      names: tuple, factors: tuple) -> list:
    """ Get students with given list of `ids` or `names` """
    factors = ('S.student_id', 'student_name', *factors)
    return self.__make_request(DBQuery.get_by(start, end, ids, names, factors))

  def get_students_by_week(self, start: str, end: str, factors: tuple) -> list:
    """ Get all students with classes on given dates """
    factors = ('S.student_id', 'student_name', *factors)
    return self.__make_request(DBQuery.get_by_week(start, end, factors))
