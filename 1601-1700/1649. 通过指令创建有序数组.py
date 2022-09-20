import collections, heapq, itertools
from typing import List


# 给你一个整数数组 instructions ，你需要根据 instructions 中的元素创建一个有序数组。一开始你有一个空的数组 nums ，你需要 从左到右 遍历 instructions 中的元素，将它们依次插入 nums 数组中。每一次插入操作的 代价 是以下两者的 较小值 ：
#
# nums 中 严格小于  instructions[i] 的数字数目。
# nums 中 严格大于  instructions[i] 的数字数目。
# 比方说，如果要将 3 插入到 nums = [1,2,3,5] ，那么插入操作的 代价 为 min(2, 1) (元素 1 和  2 小于 3 ，元素 5 大于 3 ），插入后 nums 变成 [1,2,3,3,5] 。
#
# 请你返回将 instructions 中所有元素依次插入 nums 后的 总最小代价 。由于答案会很大，请将它对 109 + 7 取余 后返回。
#
#  
#
# 示例 1：
#
# 输入：instructions = [1,5,6,2]
# 输出：1
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 5 ，代价为 min(1, 0) = 0 ，现在 nums = [1,5] 。
# 插入 6 ，代价为 min(2, 0) = 0 ，现在 nums = [1,5,6] 。
# 插入 2 ，代价为 min(1, 2) = 1 ，现在 nums = [1,2,5,6] 。
# 总代价为 0 + 0 + 0 + 1 = 1 。
# 示例 2:
#
# 输入：instructions = [1,2,3,6,5,4]
# 输出：3
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 2 ，代价为 min(1, 0) = 0 ，现在 nums = [1,2] 。
# 插入 3 ，代价为 min(2, 0) = 0 ，现在 nums = [1,2,3] 。
# 插入 6 ，代价为 min(3, 0) = 0 ，现在 nums = [1,2,3,6] 。
# 插入 5 ，代价为 min(3, 1) = 1 ，现在 nums = [1,2,3,5,6] 。
# 插入 4 ，代价为 min(3, 2) = 2 ，现在 nums = [1,2,3,4,5,6] 。
# 总代价为 0 + 0 + 0 + 0 + 1 + 2 = 3 。
# 示例 3：
#
# 输入：instructions = [1,3,3,3,2,4,2,1,2]
# 输出：4
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3,3] 。
# 插入 2 ，代价为 min(1, 3) = 1 ，现在 nums = [1,2,3,3,3] 。
# 插入 4 ，代价为 min(5, 0) = 0 ，现在 nums = [1,2,3,3,3,4] 。
# ​​​​​插入 2 ，代价为 min(1, 4) = 1 ，现在 nums = [1,2,2,3,3,3,4] 。
# 插入 1 ，代价为 min(0, 6) = 0 ，现在 nums = [1,1,2,2,3,3,3,4] 。
# 插入 2 ，代价为 min(2, 4) = 2 ，现在 nums = [1,1,2,2,2,3,3,3,4] 。
# 总代价为 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4 。
#  
#
# 提示：
#
# 1 <= instructions.length <= 105
# 1 <= instructions[i] <= 105
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/create-sorted-array-through-instructions
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        from sortedcontainers import SortedList
        ans = 0
        nums = SortedList()
        for num in instructions:
            mi, ma = nums.bisect_left(num), nums.bisect_right(num)
            ans += min(mi, len(nums) - ma)
            nums.add(num)
        return ans % (10 ** 9 + 7)


# 树状数组
class ftree:
    def __init__(self, n):
        self.li = [0] * (n + 1)
        self.n = n

    @staticmethod
    def lowbit(num):
        return num & (-num)

    def update(self, num, dt):
        while num <= self.n:
            self.li[num] += dt
            num += self.lowbit(num)

    def quiry(self, num):
        ans = 0
        while num > 0:
            ans += self.li[num]
            num -= self.lowbit(num)
        return ans

    def quiryrange(self, x, y):  # 求[x+1,y]的个数
        return self.quiry(y) - self.quiry(x)


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        import bisect
        def discretization(nums):
            a = sorted(list(set(nums)))
            return [bisect.bisect_left(a, num) + 1 for num in nums]

        lst = discretization(instructions)
        ft = ftree(max(lst))
        ans = 0
        sum_ = 0
        for num in lst:
            mi = ft.quiry(num - 1)
            ma = ft.quiry(num)
            ans += min(mi, sum_ - ma)
            sum_ += 1
            ft.update(num, 1)
        return ans % (10 ** 9 + 7)


# 线段树
class segtree:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.treesum = 0

    @property
    def _mid(self):
        return (self.l + self.r) // 2

    @property
    def _left(self):
        self.left = self.left or segtree(self.l, self._mid)
        return self.left

    @property
    def _right(self):
        self.right = self.right or segtree(self._mid + 1, self.r)
        return self.right

    def update(self, id, diff):
        self.treesum += diff
        if self.l >= self.r:
            return
        if id <= self._mid:
            self._left.update(id, diff)
        else:
            self._right.update(id, diff)

    def query(self, ql, qr):
        if qr < self.l or ql > self.r:
            return 0
        if ql <= self.l and qr >= self.r:
            return self.treesum
        return self._left.query(ql, qr) + self._right.query(ql, qr)


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        import bisect
        def discretization(nums):
            a = sorted(list(set(nums)))
            return [bisect.bisect_left(a, num) + 1 for num in nums]
        instructions=discretization(instructions)
        ub = max(instructions)
        st = segtree(1, ub)
        ans = 0
        for num in instructions:
            mi = st.query(1, num - 1)
            ma = st.query(num + 1, ub)
            ans += min(mi, ma)
            st.update(num, 1)
        return ans % (10 ** 9 + 7)
Solution().createSortedArray([1,3,3,3,2,4,2,1,2])