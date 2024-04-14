# Write your MySQL query statement below
select Max(num) as num
From
(
select num
from Mynumbers
group by num
having count(num)=1
) as t