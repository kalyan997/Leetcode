# Write your MySQL query statement below
select 
case when s1.id%2 != 0 then if(s2.id is not NULL,s2.id,s1.id)
else s1.id-1
end 
as id, s1.student as student
from seat as s1 left join seat as s2
on s1.id=s2.id-1
order by id