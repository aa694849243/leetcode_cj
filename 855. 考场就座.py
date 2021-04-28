# 在考场里，一排有 N 个座位，分别编号为 0, 1, 2, ..., N-1 。
#
#  当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，
# 那么学生就坐在 0 号座位上。)
#
#  返回 ExamRoom(int N) 类，它有两个公开的函数：其中，函数 ExamRoom.seat() 会返回一个 int （整型数据），代表学生坐的位
# 置；函数 ExamRoom.leave(int p) 代表坐在座位 p 上的学生现在离开了考场。每次调用 ExamRoom.leave(p) 时都保证有学生坐在
# 座位 p 上。
#
#
#
#  示例：
#
#  输入：["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[]
# ,[4],[]]
# 输出：[null,0,9,4,2,null,5]
# 解释：
# ExamRoom(10) -> null
# seat() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
# seat() -> 9，学生最后坐在 9 号座位上。
# seat() -> 4，学生最后坐在 4 号座位上。
# seat() -> 2，学生最后坐在 2 号座位上。
# leave(4) -> null
# seat() -> 5，学生最后坐在 5 号座位上。
#
#
#
#
#  提示：
#
#
#  1 <= N <= 10^9
#  在所有的测试样例中 ExamRoom.seat() 和 ExamRoom.leave() 最多被调用 10^4 次。
#  保证在调用 ExamRoom.leave(p) 时有学生正坐在座位 p 上。
#
#  Related Topics Ordered Map
#  👍 82 👎 0


class ExamRoom:

    def __init__(self, N: int):
        self.n = N
        self.m = set()

    def seat(self) -> int:
        if not self.m:
            self.m |= {0}
            return 0
        a = sorted(self.m)
        ma = float('-inf')
        ans = 0
        if a[0] != 0:
            ma = a[0] - 1
        for i in range(1, len(a)):
            if a[i]-a[i-1]==1:
                continue
            move = (a[i] - a[i - 1] - 2) // 2
            if move > ma:
                ma = move
                ans = a[i-1] + move + 1
        if a[-1] != self.n - 1:
            if self.n - 1 - a[-1] - 1 > ma:
                self.m.add(self.n-1)
                return self.n - 1
        self.m.add(ans)
        return ans


    def leave(self, p: int) -> None:
        self.m.discard(p)

# Your ExamRoom object will be instantiated and called as such:
obj = ExamRoom(10)
obj.seat()
obj.seat()
obj.seat()
obj.seat()
# leetcode submit region end(Prohibit modification and deletion)
