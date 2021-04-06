'''当 k 个日程安排有一些时间上的交叉时（例如 k 个日程安排都在同一时间内），就会产生 k 次预订。

给你一些日程安排 [start, end) ，请你在每个日程安排添加后，返回一个整数 k ，表示所有先前日程安排会产生的最大 k 次预订。

实现一个 MyCalendarThree 类来存放你的日程安排，你可以一直添加新的日程安排。

MyCalendarThree() 初始化对象。
int book(int start, int end) 返回一个整数 k ，表示日历中存在的 k 次预订的最大值。
 

示例：

输入：
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
输出：
[null, 1, 1, 2, 3, 3, 3]

解释：
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(50, 60); // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(10, 40); // 返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
myCalendarThree.book(5, 15); // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
myCalendarThree.book(5, 10); // 返回 3
myCalendarThree.book(25, 55); // 返回 3
 

提示：

0 <= start < end <= 109
每个测试用例，调用 book 函数最多不超过 400次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/my-calendar-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# 1差分思想 边界计数
import collections


class MyCalendarThree:

    def __init__(self):
        self.delta = collections.Counter()
        self.ans = 0

    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1
        self.delta[end] -= 1
        acc = 0
        for key in sorted(self.delta):
            acc += self.delta[key]
            if acc > self.ans:
                self.ans = acc
        return self.ans


# 2 线段树+懒惰传播 大神写法
class MyCalendarThree:
    def __init__(self):
        self.lazy = collections.defaultdict(int)
        self.tree = collections.defaultdict(int)

    def book(self, start: int, end: int) -> int:
        def update(s, e, l=0, r=10 ** 9, id=1):  # 左闭右开
            if r <= s or e <= l:
                return
            if s <= l < r <= e:  # 范围符合要求，直接更新tree和懒惰树相应节点的值
                self.lazy[id] += 1  # 懒惰树节点值储存未向下层传递的tree值
                self.tree[id] += 1
            else:  # 范围比较小，先向下更新tree和懒惰树
                mid = (l + r) // 2
                update(s, e, l, mid, 2 * id + 1)
                update(s, e, mid, r, 2 * id + 2)
                self.tree[id] = self.lazy[id] + max(self.tree[2 * id + 1], self.tree[2 * id + 2])  # tree的节点值为之前存的懒惰树节点值+下层向上层传递的tree值。

        update(start, end)
        return self.tree[1]


# 2线段树+懒惰传播 别人的写法
class SGTree():
    def __init__(self, l, r):
        self.lb = l
        self.rb = r
        self.lazy = 0
        self.mx = 0
        self.left = None
        self.right = None

    def update(self, l, r, v):
        if (l <= self.lb and r >= self.rb):
            self.mx += v
            self.lazy += v
            return
        mid = (self.lb + self.rb) / 2
        if (not self.left):
            self.left = SGTree(self.lb, mid)
            self.right = SGTree(mid + 1, self.rb)
        self.pushdown()
        if (r <= mid):
            self.left.update(l, r, v)
        elif (l > mid):
            self.right.update(l, r, v)
        else:
            self.left.update(l, r, v)
            self.right.update(l, r, v)
        self.mx = max(self.left.mx, self.right.mx)

    def pushdown(self):
        if (self.lazy != 0):
            self.left.lazy += self.lazy
            self.left.mx += self.lazy
            self.right.lazy += self.lazy
            self.right.mx += self.lazy
            self.lazy = 0


class MyCalendarThree(object):
    def __init__(self):
        self.SG = SGTree(0, 1000000000)

    def book(self, start, end):
        self.SG.update(start, end - 1, 1)
        return self.SG.mx
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
