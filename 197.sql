# Write your MySQL query statement below
SELECT W.id as Id
FROM weather as W, weather W2 
WHERE DATEDIFF(W.recordDate, W2.recordDate)=1 and W.Temperature > W2.Temperature