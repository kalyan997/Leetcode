# Write your MySQL query statement below
select C.name as Customers
from Customers as C
where C.id not in
(
    select customerId
    from Orders
)