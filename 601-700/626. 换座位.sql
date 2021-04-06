-- https://leetcode-cn.com/problems/exchange-seats/solution/huan-zuo-wei-by-leetcode/
-- 1 case语句
select (case when mod(id,2)=1 and id != counts then id+1
 when mod(id,2)=1 and id=counts then id
 else id-1
 end) id,student
 from seat,(select count(*) counts from seat) as count_seats
 order by id asc
-- 2 coalesce()语句
select a.id,coalesce(b.student,a.student) as student from seat a
left join seat b
on (a.id+1)^1-1=b.id
order by id asc
-- 3这种情况用coalesce不行
select a.id,coalesce(b.student,a.student) from seat a,seat b where (a.id-b.id=-1 and mod(a.id,2)=1) or (a.id-b.id=1 and mod(a.id,2)=0)
order by a.id