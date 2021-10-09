-- # Write your MySQL query statement below
select * from cinema a where mod(a.id,2)=1 and a.description !='boring' order by a.rating desc