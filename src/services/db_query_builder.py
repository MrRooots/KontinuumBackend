class DBQuery:
  """ SQL queries builder """

  @staticmethod
  def build_and_query(ids: tuple = None, names: tuple = None) -> str:
    """ Build and query for specific students names OR ids """
    if ids:
      t = len(ids) == 1
      and_query = f"S.student_id {f'= {ids[0]}' if t else f'in {ids}'}"
    else:
      t = len(names) == 1
      and_query = "S.student_name {}".format(
        f'= \'{names[0]}\'' if t else f'in {names}')

    return and_query

  @staticmethod
  def get_by_week(start: str, end: str, factors: tuple) -> str:
    """ Build query for selecting all students for given week """
    return f"""
      select {('{}, ' * len(factors)).format(*factors)[:-2]}
      from Student S
         inner join ClassesData CD on CD.student_id = S.student_id
         inner join GroupStudentTest GST on CD.group_id = GST.group_id 
                                          and CD.student_id = GST.student_id
      where date between '{start}' and '{end}' order by S.student_id
    """

  @staticmethod
  def get_by(start, end, ids, names, factors) -> str:
    """ Build query to select students with specific names OR ids """
    and_query = DBQuery.build_and_query(ids, names)

    return f"""
      select {('{}, ' * len(factors)).format(*factors)[:-2]}
      from Student S
         inner join ClassesData CD on CD.student_id = S.student_id
         inner join GroupStudentTest GST on CD.group_id = GST.group_id 
                                          and CD.student_id = GST.student_id
      where date between '{start}' and '{end}' and {and_query} 
      order by S.student_id
    """
