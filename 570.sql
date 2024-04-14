# Write your MySQL query statement below
select E2.name as name
From Employee as E1, Employee as E2
WHERE E1.managerId = E2.id
GROUP BY E1.managerId
HAVING COUNT(E1.managerId)>=5