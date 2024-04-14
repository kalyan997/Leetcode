# Write your MySQL query statement below
with red_companies as
(
    select C.com_id
    from Company as C
    where C.name = "Red"
),

sales_with_red as 
(
    select O.sales_id as sales_id
    from Orders as O
    where O.com_id in (select * from red_companies)
)
    select S.name as name
    from SalesPerson as S
    where S.sales_id not in (select * from sales_with_red)
