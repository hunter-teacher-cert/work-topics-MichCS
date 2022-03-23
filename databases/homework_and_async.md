## SQL Homework: 

### First Part/Homework:

sql_query_string = """

SELECT s.first, s.last, s.studentID, s.grade, s.ScanTime, s.status, p.date, p.courseSection, p.attendance, p.period, p.teacher, substr(s.scanTime, 1,instr(s.scanTime, ' ')-1) as scanDate
FROM scan as s
INNER JOIN periodAtt as p
on s.studentID=p.studentID AND p.Attendance = 'A' and substr(s.scanTime, 1,instr(s.scanTime, ' ')-1) = p.date order by s.last ASC
"""

### SQL ASYNC Challenge #2

SELECT *
FROM (
SELECT s.first, s.last, s.studentID, s.grade, s.ScanTime, s.status, p.date, p.courseSection, p.attendance, p.period,
p.teacher, substr(s.scanTime, 1,instr(s.scanTime, ' ')-1) as scanDate
FROM scan as s
INNER JOIN periodAtt as p
on s.studentID=p.studentID AND p.Attendance = 'A' and substr(s.scanTime, 1,instr(s.scanTime, ' ')-1) = p.date
order by s.last ASC )
as allCuts
INNER JOIN bio as b
on allCuts.studentID=b.StudentID

### [Homework Resource/Click Me](https://colab.research.google.com/drive/12ZHMqMEED_slTcaSyJex2-Q7KggaQkug?usp=sharing)
