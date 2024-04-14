# Write your MySQL query statement below

WITH cte1 AS (
    SELECT A1.player_id AS player_id, MIN(A1.event_date) as first_date
    FROM Activity AS A1
    GROUP BY A1.player_id
),

cte2 as 
(
  SELECT A1.player_id AS player_id, A2.first_date as first_date, A1.event_date as next_date
    FROM Activity AS A1, cte1 AS A2 
    WHERE A1.player_id = A2.player_id and A2.first_date < A1.event_date and DATEDIFF(A1.event_date, A2.first_date) = 1
)


SELECT ROUND(COUNT(DISTINCT cte2.player_id) / COUNT(DISTINCT A.player_id), 2) AS fraction
FROM Activity AS A
LEFT JOIN cte2 ON A.player_id = cte2.player_id;