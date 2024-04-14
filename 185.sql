# Write your MySQL query statement below
with cte1 as
(
    select e.*, dense_rank() over(partition by DepartmentId order by Salary desc) as DeptRank
    from Employee e
)

select d.name as Department, c.name as Employee, c.salary as salary
from cte1 as c, Department as d
where c.departmentId = d.id and c.DeptRank<=3