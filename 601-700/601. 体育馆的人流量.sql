select distinct t1.* from stadium t1, stadium t2, stadium t3
where t1.people >= 100 and t2.people >= 100 and t3.people >= 100
and ((t1.id-t2.id=1 and t1.id-t3.id=]=2 and t2.id-t3.id=1) or -- t1高峰第3天
(t2.id-t1.id=1 and t1.id-t3.id=1) or -- t1高峰第二天
(t3.id-t2.id=1 and t2.id-t1.id=1)) -- t1高峰第一天
order by t1.id

