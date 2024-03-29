/*Trips 表中存所有出租车的行程信息。每段行程有唯一键 Id，Client_Id 和 Driver_Id 是 Users 表中 Users_Id 的外键。Status 是枚举类型，枚举成员为 (‘completed’, ‘cancelled_by_driver’, ‘cancelled_by_client’)。

+----+-----------+-----------+---------+--------------------+----------+
| Id | Client_Id | Driver_Id | City_Id |        Status      |Request_at|
+----+-----------+-----------+---------+--------------------+----------+
| 1  |     1     |    10     |    1    |     completed      |2013-10-01|
| 2  |     2     |    11     |    1    | cancelled_by_driver|2013-10-01|
| 3  |     3     |    12     |    6    |     completed      |2013-10-01|
| 4  |     4     |    13     |    6    | cancelled_by_client|2013-10-01|
| 5  |     1     |    10     |    1    |     completed      |2013-10-02|
| 6  |     2     |    11     |    6    |     completed      |2013-10-02|
| 7  |     3     |    12     |    6    |     completed      |2013-10-02|
| 8  |     2     |    12     |    12   |     completed      |2013-10-03|
| 9  |     3     |    10     |    12   |     completed      |2013-10-03|
| 10 |     4     |    13     |    12   | cancelled_by_driver|2013-10-03|
+----+-----------+-----------+---------+--------------------+----------+
Users 表存所有用户。每个用户有唯一键 Users_Id。Banned 表示这个用户是否被禁止，Role 则是一个表示（‘client’, ‘driver’, ‘partner’）的枚举类型。

+----------+--------+--------+
| Users_Id | Banned |  Role  |
+----------+--------+--------+
|    1     |   No   | client |
|    2     |   Yes  | client |
|    3     |   No   | client |
|    4     |   No   | client |
|    10    |   No   | driver |
|    11    |   No   | driver |
|    12    |   No   | driver |
|    13    |   No   | driver |
+----------+--------+--------+
写一段 SQL 语句查出 2013年10月1日 至 2013年10月3日 期间非禁止用户的取消率。基于上表，你的 SQL 语句应返回如下结果，取消率（Cancellation Rate）保留两位小数。

取消率的计算方式如下：(被司机或乘客取消的非禁止用户生成的订单数量) / (非禁止用户生成的订单总数)

+------------+-------------------+
|     Day    | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 |       0.33        |
| 2013-10-02 |       0.00        |
| 2013-10-03 |       0.50        |
+------------+-------------------+

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trips-and-users
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。*/
-- 解法1
select request_at as 'Day',round(
sum(if(t.status='completed',0,1))/count(t.status),2
) as 'Cancellation Rate'
from trips t join users u1 on (u1.users_id= t.client_id and u1.banned='No')
join users u2 on (u2.users_id=t.driver_id and u2.banned='No')
where t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at order by 'Day'
-- 解法2
select request_at as 'Day',round(
sum(if(t.status='completed',0,1))/count(t.status),2
) as 'Cancellation Rate'
from trips t left join (select users_id from users where banned='Yes') a
on t.client_id=a.users_id
left join  (select  users_id from users where banned='Yes') b
on t.driver_id=b.users_id
where a.users_id is NULL and b.users_id is NULL and t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at order by 'Day'
-- 解法3
select request_at as 'Day',round(
sum(if(t.status='completed',0,1))/count(t.status),2
) as 'Cancellation Rate'
from trips AS t
where t.client_id not in (select users_id from users where banned='Yes') and
t.driver_id not in (select users_id from users where banned='Yes')
and t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at  order by 'Day'