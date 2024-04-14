# Write your MySQL query statement below
select C.class
from Courses as C
group by C.class
having count(C.student)>=5