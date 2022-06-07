-------------------------------------- Recreate all tables with data
drop table if exists Student;
drop table if exists "Group";
drop table if exists GroupStudentTest;
drop table if exists ClassesData;

create table Student
(
    student_id   integer primary key,
    student_name text not null
);

create table 'Group'
(
    group_id   integer primary key,
    group_name text not null
);

create table GroupStudentTest
(
    group_id   integer not null,
    student_id integer not null,
    test       integer not null,
    foreign key (group_id) references 'Group' (group_id),
    foreign key (student_id) references Student (student_id)
);

create table ClassesData
(
    date       text    not null,
    group_id   integer not null,
    student_id integer not null,
    activity   integer not null,
    homework   integer not null,
    foreign key (group_id) references 'Group' (group_id),
    foreign key (student_id) references Student (student_id)
);

insert into Student (student_id, student_name)
values (1, 'Алексей'),
       (2, 'Мария'),
       (3, 'Николай'),
       (4, 'Михаил'),
       (5, 'Елена');

insert into "Group" (group_id, group_name)
values (1, 'Математика ЕГЭ'),
       (2, 'Русский язык ЕГЭ');

insert into GroupStudentTest (group_id, student_id, test)
values (1, 1, 74),
       (1, 2, 68),
       (1, 4, 33),
       (2, 1, 45),
       (2, 2, 56),
       (2, 3, 62),
       (2, 5, 56);

INSERT INTO ClassesData (date, group_id, student_id, activity, homework)
values ('2021-09-27', 1, 1, 5, 100),
       ('2021-09-27', 1, 2, 3, 91),
       ('2021-09-27', 1, 4, 3, 45),
       ('2021-09-30', 2, 5, 3, 60),
       ('2021-09-30', 2, 2, 1, 25),
       ('2021-09-30', 2, 3, 1, 35),
       ('2021-09-30', 2, 1, 4, 10),
       ('2021-10-04', 1, 1, 2, 73),
       ('2021-10-04', 1, 2, 4, 58),
       ('2021-10-04', 1, 4, 3, 82),
       ('2021-10-07', 2, 5, 5, 80),
       ('2021-10-07', 2, 2, 5, 90),
       ('2021-10-07', 2, 3, 5, 100),
       ('2021-10-07', 2, 1, 4, 95),
       ('2021-10-11', 1, 1, 4, 45),
       ('2021-10-11', 1, 2, 4, 10),
       ('2021-10-11', 1, 4, 3, 15),
       ('2021-10-14', 2, 5, 2, 35),
       ('2021-10-14', 2, 2, 3, 85),
       ('2021-10-14', 2, 3, 4, 70),
       ('2021-10-14', 2, 1, 5, 63),
       ('2021-10-19', 1, 1, 5, 90),
       ('2021-10-19', 1, 2, 3, 55),
       ('2021-10-19', 1, 4, 5, 60),
       ('2021-10-21', 2, 5, 3, 34),
       ('2021-10-21', 2, 2, 3, 76),
       ('2021-10-21', 2, 3, 3, 88),
       ('2021-10-21', 2, 1, 5, 50),
       ('2021-10-22', 2, 5, 3, 40),
       ('2021-10-22', 2, 2, 3, 85),
       ('2021-10-22', 2, 3, 3, 100),
       ('2021-10-22', 2, 1, 5, 75);

-- Add new column to check flexibility (just modify Configuration.FACTORS) and add __calculate_new_param to models.Lesson
-- alter table ClassesData add column new_param default 0;
-- update ClassesData set new_param = homework - 14;

-------------------------------------- Create new group and relations for testing

insert into "Group" values (3, 'Новая группа');

insert into GroupStudentTest values (3, 1, 64);

insert into ClassesData (date, group_id, student_id, activity, homework) values ('2021-10-19', 3, 1, 3, 91);

select * from "Group";
select * from GroupStudentTest;
select * from ClassesData;

-- Main Query
select date, CD.group_id, S.student_id, student_name, activity, homework, test
from Student S
         inner join ClassesData CD on CD.student_id = S.student_id
         inner join GroupStudentTest GST on CD.group_id = GST.group_id and CD.student_id = GST.student_id
where strftime('%Y.%m.%d', date) between '2021.09.27' and '2021.10.04';

-- Main Query
select student_id,
       student_name,
       sum(activity) as total_activity,
       sum(homework) as total_homework,
       test
from (select S.student_id, student_name, activity, homework, test
      from Student S
               inner join ClassesData CD on CD.student_id = S.student_id
               inner join GroupStudentTest GST on CD.group_id = GST.group_id and CD.student_id = GST.student_id
      where date between '18.10.2021' and '24.10.2021')
group by student_name
order by student_id;

-- Some tests
select date
from Student S
         inner join ClassesData CD on CD.student_id = S.student_id
         inner join GroupStudentTest GST on CD.group_id = GST.group_id
    and CD.student_id = GST.student_id
where date between '2021-09-27' and '2021-10-03';
