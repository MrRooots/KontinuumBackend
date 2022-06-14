class WeekDates:
  """ Week dates container """

  def __init__(self, start, end) -> None:
    self.start = start
    self.end = end

  @property
  def values(self) -> tuple:
    """ Get start and end dates of the week """
    return self.start, self.end
