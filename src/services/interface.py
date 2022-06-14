import tkinter as tk

FONT = ("Arial Bold", 16)
L_FONT = ("Arial Bold", 12)
DATE = ('Day', 'Month', 'Year')
STUDENT_PARAMS = ('Ids', 'Names')

DATES = None
STUDENTS_IDS = None
STUDENTS_NAMES = None


class Interface:
  """ Interface implementation """

  @staticmethod
  def get_dates(inputs: list[tk.Entry]) -> str:
    """ Clear data from inputs """
    return '.'.join(
      txt.get() if len(txt.get()) >= 2 else '0' + txt.get()
      for txt in reversed(inputs))

  @staticmethod
  def clicked(window: tk.Tk, inputs: list[tk.Entry],
              students: list[tk.Entry]) -> None:
    """ Handle 'Calculate' button click. Set the dates and students params """
    global DATES, STUDENTS_IDS, STUDENTS_NAMES
    try:
      DATES = Interface.get_dates(inputs)
    except:
      DATES = '2021.10.24'
    finally:
      if len(DATES) < 10:
        DATES = '2021.10.24'

    try:
      s = [txt.get() for txt in students]
      print(s)
      if s.count('') == 2:
        s = None
      else:
        try:
          STUDENTS_IDS = [int(i) for i in s[0].replace(' ', '').split(',')]
        except ValueError:
          STUDENTS_NAMES = [i for i in s[1].replace(' ', '').split(',')]
    except:
      s = None

    window.destroy()

  @staticmethod
  def build_date_input(window: tk.Tk,
                       title: str, label: str,
                       values: tuple, start_from: int = 0) -> list[tk.Entry]:
    """ Build data inputs """
    inputs = []
    tk.Label(window,
             text=title, font=FONT).grid(column=start_from, row=0)

    for idx, text in enumerate(values):
      tk.Label(window,
               text=f'{label} {text}: ',
               font=L_FONT).grid(column=start_from, row=idx + 1,
                                 sticky="W")

      _input = tk.Entry(window, width=15)
      _input.grid(column=start_from + 1, row=idx + 1)

      inputs.append(_input)

    return inputs

  @staticmethod
  def run_with_interface() -> tuple:
    """ Run script with interface """
    window = tk.Tk()

    window.title('Score calculator')
    window.geometry('800x300')

    dates = Interface.build_date_input(window,
                                       title='Enter last week date: ',
                                       label='Enter week',
                                       values=DATE)
    students = Interface.build_date_input(window,
                                          title='Specify students names OR ids: ',
                                          label='Enter student',
                                          values=STUDENT_PARAMS,
                                          start_from=3)

    tk.Button(window, text='Calculate',
              command=lambda: Interface.clicked(window, dates, students),
              padx=25, pady=10).grid(column=0, row=5)

    window.mainloop()

    return DATES, STUDENTS_IDS, STUDENTS_NAMES

  @staticmethod
  def show_popup() -> None:
    """ Show popup window if there are no any records """
    window = tk.Tk()
    window.title('There are no any records!')
    window.geometry('350x100')

    tk.Label(window,
             text='There are no any records that matches your query!',
             font=L_FONT).grid(column=0, row=0)

    tk.Button(window, text='Understood',
              command=window.destroy,
              padx=25, pady=10).grid(column=0, row=1)

    window.mainloop()
