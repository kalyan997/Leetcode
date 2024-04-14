# Write your MySQL query statement below
with cte1 as
(
    select R.requester_id as id, count(R.accepter_id) as num
    from RequestAccepted as R
    group by R.requester_id
),
cte2 as
(
    select R.accepter_id as id, count(R.requester_id) as num
    from RequestAccepted as R
    group by R.accepter_id
),
cte3 as 
(
    select * from cte1
    UNION ALL
    select * from cte2
)
select id as id, sum(num) as num
from cte3
group by id
order by num desc
limit 1
