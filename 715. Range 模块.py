'''Range 模块是跟踪数字范围的模块。你的任务是以一种有效的方式设计和实现以下接口。

addRange(int left, int right) 添加半开区间 [left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。
queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true。
removeRange(int left, int right) 停止跟踪区间 [left, right) 中当前正在跟踪的每个实数。
 

示例：

addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true （区间 [10, 14) 中的每个数都正在被跟踪）
queryRange(13, 15): false （未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
queryRange(16, 17): true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）
 

提示：

半开区间 [left, right) 表示所有满足 left <= x < right 的实数。
对 addRange, queryRange, removeRange 的所有调用中 0 < left < right < 10^9。
在单个测试用例中，对 addRange 的调用总数不超过 1000 次。
在单个测试用例中，对  queryRange 的调用总数不超过 5000 次。
在单个测试用例中，对 removeRange 的调用总数不超过 1000 次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-module
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 1treemap
# a[0:0]=x 相当于在0位插入1个x a[inf:inf]相当于在尾部插入1个x a[i:j+1]相当于将i:j+1的值变为x
import bisect


class RangeModule:

    def __init__(self):
        self.range = []

    def _bound(self, l, r):
        i, j = 0, len(self.range) - 1
        for d in (100, 10, 1):
            while i + d - 1 < len(self.range) and self.range[i + d - 1][1] < l:
                # 循环结束range[i-1][1]<l,那么range[i][1]>=l,i可以接受
                i += d
            while j - d + 1 >= 0 and self.range[j - d + 1][0] > r:
                # 循环结束range[j+1][0]>r,那么range[j][0]<=r,j同样可以接受
                j -= d
        return i, j  # 假如l过大没有交集，那么i+1-1即i==len(range)，j==len(range)-1;假如r过小，那么同样j-1+1==-1,i=0

    def addRange(self, left: int, right: int) -> None:
        i, j = self._bound(left, right)
        if i <= j:  # 避免空集或找不到交集
            left = min(self.range[i][0], left)
            right = max(self.range[j][1], right)
        self.range[i:j + 1] = [(left, right)]

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_left(self.range, (left, float('inf')))
        if i:
            i -= 1
        else:
            return False
        if not self.range:
            return False
        return True if left >= self.range[i][0] and right <= self.range[i][1] else False

    def removeRange(self, left: int, right: int) -> None:
        i, j = self._bound(left, right)
        merge = []
        for k in range(i, j + 1):
            if self.range[k][0] < left:
                merge.append((self.range[k][0], left))
            if self.range[k][1] > right: #这里如果填等于的话也没错但是如果等于的话range[k][1]和right都是取不到的
                merge.append((right, self.range[k][1]))
        self.range[i:j + 1] = merge


# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(38, 98)
obj.addRange(3, 18)
obj.removeRange()
obj.addRange(43, 90)
obj.queryRange(57,96)
# ["RangeModule","addRange","addRange","removeRange","addRange","addRange","queryRange"]
# [[],[38,98],[8,33],[3,71],[6,57],[43,90],[57,96]]
