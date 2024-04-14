# Write your MySQL query statement below
SELECT E.name as name, B.bonus as bonus
FROM Employee as E LEFT JOIN Bonus as B
ON E.empId = B.empId
WHERE B.bonus < 1000 or B.bonus is NULL