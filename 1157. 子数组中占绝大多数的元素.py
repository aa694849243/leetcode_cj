# -*- coding: utf-8 -*-
# 实现一个 MajorityChecker 的类，它应该具有下述几个 API：
#
#
#  MajorityChecker(int[] arr) 会用给定的数组 arr 来构造一个 MajorityChecker 的实例。
#  int query(int left, int right, int threshold) 有这么几个参数：
#
#  0 <= left <= right < arr.length 表示数组 arr 的子数组的长度。
#  2 * threshold > right - left + 1，也就是说阈值 threshold 始终比子序列长度的一半还要大。
#
#
#
#
#  每次查询 query(...) 会返回在 arr[left], arr[left+1], ..., arr[right] 中至少出现阈值次数 thresh
# old 的元素，如果不存在这样的元素，就返回 -1。
#
#
#
#  示例：
#
#  MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
# majorityChecker.query(0,5,4); // 返回 1
# majorityChecker.query(0,3,3); // 返回 -1
# majorityChecker.query(2,3,2); // 返回 2
#
#
#
#
#  提示：
#
#
#  1 <= arr.length <= 20000
#  1 <= arr[i] <= 20000
#  对于每次查询，0 <= left <= right < len(arr)
#  对于每次查询，2 * threshold > right - left + 1
#  查询次数最多为 10000
#
#  Related Topics 线段树 数组 二分查找
#  👍 48 👎 0
import bisect
import collections
from typing import List


class seg:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self._left = None
        self._right = None
        self.val = float('-inf')

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or seg(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or seg(self.mid, self.end)
        return self._right

    def query(self, left, right, arr, m):
        def ismajority(elem):  # 计算elem是不是left-right范围的绝对众数
            l = bisect.bisect_left(m[elem], left)
            r = bisect.bisect_right(m[elem], right - 1)
            return 2 * (r - l) > right - left

        if left >= right:
            return -1
        res = -1
        if left == self.start and right == self.end:
            if left == right - 1:
                self.val = arr[left]
            elif self.val == float('-inf'):  # 这个区间没有计算出绝对众数,开始计算self.val
                elem1 = self.left.query(left, self.mid, arr, m)
                elem2 = self.right.query(self.mid, right, arr, m)
                if elem1 != -1 and ismajority(elem1):
                    self.val = elem1
                elif elem2 != -1 and ismajority(elem2):
                    self.val = elem2
                else:
                    self.val = -1
            res = self.val
        else:  # 非标准的区间，即不完整属于左节点或右节点的区间，因为不属于任何节点，不存储self.val
            elem1 = self.left.query(left, min(self.mid, right), arr, m)
            elem2 = self.right.query(max(self.mid, left), right, arr, m)
            if elem1 != -1 and ismajority(elem1):
                res = elem1
            elif elem2 != -1 and ismajority(elem2):
                res = elem2
        return res


class MajorityChecker:

    def __init__(self, arr: List[int]):
        m = collections.defaultdict(list)
        for i, val, in enumerate(arr):
            m[val].append(i)
        self.seg = seg(0, len(arr))
        self.m = m
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        elem = self.seg.query(left, right + 1, self.arr, self.m)
        l = bisect.bisect_left(self.m[elem], left)
        r = bisect.bisect_right(self.m[elem], right)
        return elem if r - l >= threshold else -1


# Your MajorityChecker object will be instantiated and called as such:
obj = MajorityChecker([1, 1, 2, 2, 1, 1])
obj.query(0, 5, 4)
# leetcode submit region end(Prohibit modification and deletion)
