# Write your MySQL query statement below
select A.player_id as player_id, min(A.event_date) as first_login
from Activity as A
group by A.player_id