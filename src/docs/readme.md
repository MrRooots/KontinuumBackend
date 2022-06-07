# Implemented

### Installing dependencies
In `CMD` from `KontinuumBackend/` folder: `pip install -r requirements.txt`. 

External dependencies are: `pandas + openpyxl` for excel writing.

### Input Data
Since there were no specific requirements for the method of storing/reading input data
I decide to store it as `SQLite` tables, according to template data from test task.

Also **important note**: again, because i use `SQLite` the dates have to be 
entered into database in `YYYY-MM-DD` format! 

**P.S**: Hope that's not really critical. (**fix**: use another SQL engine with `date` type support, for example)

### Launching
Launch script by `python -m src.manage [-from={last week date}] [-ids=[1,...] OR -names=[Name,...]]`
    
For example: `python -m src.manage -from=24.10.2021`, date `DD.MM.YYYY` format is **required**!
Inside script, due to the fact that I use `SQLite` db the dates will be converted in `YYYY-MM-DD` format.

The calculations for this command will be performed for all students with lessons for `'2021-10-18' :: '2021-10-24'` week.

To get points of concrete students for lessons this week: `python -m src.manage -from=24.10.2021 -ids=[1,2,5]` or
`python -m src.manage -from=18.10.2021 -names=[name1,name2]`

To collect data from interface: `python -m src.manage -interface`. 
You can specify date, the `24.10.2021` will be used otherwise. 
Also you can specify the ids OR names of students in `Enter student ids [names]`field : `id1, id2` OR `name1, name2`

**P.S**: You can find database structure\fillers and all main queries in `src/docs/db_structure.sql` file.

### Flexibility   
The script is flexible for adding students\groups\lessons\params **into existing tables**.
 
If you want to add new **group\student\lesson\etc** check `src/docs/db_structure.sql` lines `98-105`.

If you want to add new **calculation parameter** you need to a new column to `ClassesData` table.
check `src/docs/db_structure.sql` lines `93-94`. 
Suppose, that you've added column called `new_param`. 
Now to use its values in calculations you have to:
  1. Inside `src.config.config.Configuration` add `new_param` to `FACTORS` tuple.
  2. Inside `src.core.models.Lesson` add `__calculate_new_param` method with return of `int` or `float`.
  3. That's it, now the `new_param` column will participate in **all** calculations.

Two main calculation methods. Their logic implementation can be found in: `src/core/data_source.py` 
file + SQL queries from: `src/services/db_query_builder.py` file.
  1. `get_students_by_week()` - calculate the total score for all students who had lessons this week.
  2. `get_students_by({ ids=() or names=() })` - calculate the total score only for given students for lessons this week.
  3. Also there is a `Utils.open_as_excel()` method, that will create `src.config.config.Configuration.EXCEL_FILE_NAME`
     excel file and open it (opening tested on WIN with installed excel only)
 
## Documentation
All functions/methods/classes have docstring in their definition.