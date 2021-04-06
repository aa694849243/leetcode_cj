'''给定一个非负整数的数据流输入 a1，a2，…，an，…，将到目前为止看到的数字总结为不相交的区间列表。

例如，假设数据流中的整数为 1，3，7，2，6，…，每次的总结为：

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
 

进阶：
如果有很多合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?

提示：
特别感谢 @yunhong 提供了本问题和其测试用例。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
from typing import List
import bisect


class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []  # 左边界
        self.r = []  # 右边界

    def addNum(self, val: int) -> None:
        i = bisect.bisect(self.l, val)
        if i < len(self.l):  # 正常情况，找到大于目标值的左边界
            if i - 1 >= 0:  # 目标值大于等于第一个左边界的情况
                if val - self.r[i - 1] > 1:  # 目标值比上一个右边界大超过1
                    if self.l[i] - val > 1:  # 左边界比目标值大超过1
                        self.l.insert(i, val)
                        self.r.insert(i, val)
                    elif self.l[i] - val == 1:  # 左边界比目标值刚好大1，更新左边界
                        self.l[i] = val
                elif val - self.r[i - 1] == 1:  # 目标值比上一个右边界刚好大一
                    self.r[i - 1] = val
                if self.l[i] - self.r[i - 1] == 1:  # 更新完了还需要再考察，左边界和上一个右边界是否合并
                    self.r.pop(i - 1)
                    self.l.pop(i)
            if i == 0:  # 如果刚好插入到0，则说明第一个左边界就大于目标值了
                if self.l[i] - val > 1:
                    self.l.insert(0, val)
                    self.r.insert(0, val)
                elif self.l[i] - val == 1:
                    self.l[i] = val
        else:  # 如果空序列，或目标值大于最后一个右边界的情况
            if not self.l or val - self.r[-1] > 1:
                self.l.append(val)
                self.r.append(val)
            elif val - self.r[-1] == 1:
                self.r[-1] = val

    def getIntervals(self) -> List[List[int]]:
        return zip(self.l, self.r)


# 一个列表的思路
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def addNum(self, val: int) -> None:
        if not self.data:
            self.data.append(val)
            self.data.append(val)
        else:
            idx = self.bsh(val)
            # 二分法查的是从左到右大于等于目标值的第一个索引
            # 需要注意，数组的一对，索引为 偶数奇数，偶数是左边界，奇数是右边界
            if idx % 2 == 1:
                if self.data[idx] < val:
                    # 只会发生在查到了数组的最后一个数字
                    if val - self.data[idx] > 1:
                        self.data.append(val)
                        self.data.append(val)
                    else:
                        self.data[idx] = val
                # 如果 self.data[idx] >= val
                # 因为索引是奇数，说明前一个索引的值肯定比目标值小，此时就在区间内，无需更新
            else:
                # 此时查在偶数数索引上
                if val < self.data[idx]:
                    # 可能情况为 [1, 1, 6, 7] 查 3
                    # 变为 [1, 1, 3, 3, 6, 7]
                    if self.data[idx] - val > 1:
                        self.data.insert(idx, val)
                        self.data.insert(idx, val)
                    else:
                        # 情况为 [1, 4, 6, 7] 查5
                        # 变为 [1, 4, 5, 7]
                        self.data[idx] = val
                # 在变为 [1, 4, 5, 7] 的情况下，需要和前一种合并
                # [1,4,5,5,7,7] idx=2 先pop(2)再pop(1)
                if idx > 0 and self.data[idx] - self.data[idx - 1] == 1:
                    self.data.pop(idx)
                    self.data.pop(idx - 1)

    def getIntervals(self) -> List[List[int]]:
        return zip(self.data[::2], self.data[1::2])

    def bsh(self, target):
        l, r = 0, len(self.data) - 1
        while l < r:
            mid = (r + l) >> 1
            if self.data[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l


# 作者：YesOhh
# 链接：https: // leetcode - cn.com / problems / data - stream -as-disjoint - intervals / solution / python - wei - hu - shu - zu - jin - xing - er - fen - cha - zhao - bing /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

a = SummaryRanges()
a.addNum(1)
a.addNum(0)
