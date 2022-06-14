from src.config.config import Configuration


class Lesson:
  """ Implementation of one specific lesson """
  __slots__ = Configuration.FACTORS

  def __init__(self, values: dict = None) -> None:
    """
    Dynamic attributes creation.
    The attributes have to be specified inside
    config.config.Configuration.FACTORS variable
    """
    for attr_name in Configuration.FACTORS:
      setattr(self, attr_name, values[attr_name])

  @property
  def __calculate_activity(self) -> float:
    """ Calculate the activity points for this lesson """
    if self.activity in [4, 5]:
      return 1
    elif self.activity in [2, 3]:
      return .5
    else:
      return 0

  @property
  def __calculate_homework(self) -> float:
    """ Calculate the homework points for this lesson """
    if self.homework == 100:
      return 3
    elif 80 <= self.homework < 100:
      return 2
    elif 50 <= self.homework < 80:
      return 1
    elif self.homework < 30:
      return -.5
    else:
      return 0

  @property
  def __calculate_test(self) -> float:
    """ Calculate the test points for this lesson """
    return self.test * .02

  # @property
  # def __calculate_new_param(self) -> float:
  #   """ Calculate the new_param points for this lesson """
  #   return self.new_param * .5

  @property
  def __calculations(self) -> tuple:
    """ Get all calculations results """
    return tuple(
      getattr(self, f'_{self.__class__.__name__}__calculate_{factor}')
      for factor in Configuration.FACTORS
    )

  @property
  def total_score(self) -> float:
    """ Calculate the total score for this lesson """
    return round(sum(self.__calculations), 3)

  def __str__(self) -> str:
    """ Custom string conversion """
    return f'A: {self.activity}, H: {self.homework}, T: {self.test}'


class Student:
  """ Implementation of the student model """
  id = None
  name = None
  lessons = None

  def __init__(self, _id: int, name: str, lessons: list[Lesson] = None) -> None:
    """ Constructor """
    lessons = [] if lessons is None else lessons
    self.id = _id
    self.name = name
    self.lessons = lessons

  def __str__(self) -> str:
    """ Custom string conversion """
    return self.name

  @property
  def total_points(self) -> float:
    """ Calculate student points for this week lesson """
    return round(
      sum(lesson.total_score for lesson in self.lessons) / len(self.lessons), 3
    )
