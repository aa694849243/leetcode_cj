'''给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

说明:
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

示例:

输入: nums = [-2,5,-1], lower = -2, upper = 2,
输出: 3
解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-range-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

# 方法汇总 https://leetcode-cn.com/problems/count-of-range-sum/solution/327qu-jian-he-de-ge-shu-ti-jie-zong-he-by-xu-yuan-/
# 1 插入法
import bisect
import itertools


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefixsum = [0, *itertools.accumulate(nums, int.__add__)]
        res = 0
        m = []
        for i in range(len(prefixsum) - 1, -1, -1):
            l = bisect.bisect_left(m, prefixsum[i] + lower)  # lower<=prefixsum[j]-prefixsum[j-x]<=upper->i=j-x
            r = bisect.bisect_right(m, prefixsum[i] + upper)
            res += r - l
            bisect.insort_left(m, prefixsum[i])
        return res

Solution().countRangeSum([9, 3, 8, 19, 23, 22, 18], -22, 218)

# 2 树状数组 fenwick树
from collections import Counter


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # nlogn解法
        def query(i, base):
            q = 0
            while i > 0:
                q += base[i]
                i -= i & (-i)
            return q

        def insert(i, base):
            while i < len(base):
                base[i] += 1
                i += i & (-i)

        if lower > upper:
            return 0
        a = lower
        b = upper
        sums = [0]
        esums = [0, -a, -b]
        s = 0
        for n in nums:
            s += n
            sums += [s]
            esums += [s, s - a, s - b]
        esums.sort()
        rank = {}
        r = 1
        for s in esums:
            if s not in rank:
                rank[s] = r
                r += 1
        base = [0] * (1 + len(rank))

        insert(rank[0], base)
        c = 0
        for n, s in enumerate(sums[1:]):
            c += query(rank[s - a], base) - query(rank[s - b] - 1, base)
            insert(rank[s], base)
        return c


# caojie
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def quiry(num, base):
            val = 0
            while num > 0:
                val += base[num]
                num -= num & (-num)
            return val

        def update(num, base):
            while num <= len(rank):
                base[num] += 1
                num += num & (-num)

        prefix = [0, *itertools.accumulate(nums)]
        rank = {}
        treeval = []
        for i in prefix:
            treeval.extend([i + lower, i, i + upper])
        treeval.sort()
        x = 1
        for i in treeval:
            if i not in rank:
                rank[i] = x
                x += 1
        base = [0] * (1 + len(rank))
        res = 0
        for i in range(len(prefix) - 1, 0, -1):
            update(rank[prefix[i]], base)
            res += quiry(rank[prefix[i - 1] + upper], base) - quiry(rank[prefix[i - 1] + lower] - 1, base)
        return res


# 3 AVL树
# 思路看下汇总题解里面的第二个解法
from bintrees import avltree


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = 0
        a = avltree.AVLTree()
        a.insert(0, 0)
        res = 0
        for i in nums:
            prefix += i
            if prefix - lower < a.min_key() or prefix - upper > a.max_key(): #lower<=prefix-x<=upper-->lower+x<=prefix<=upper+x-->prefix-lower>=x,prefix-upper<=x-->不符合 prefix-lower<a.min,prefix-upper>a.max
                a.insert(prefix, prefix)
            else:
                res += list(a.keys()).index(a.floor_key(prefix - lower)) - list(a.keys()).index(
                    a.ceiling_key(prefix - upper)) + 1
                a.insert(prefix, prefix)
        return res


Solution().countRangeSum([9, 3, 8, 19, 23, 22, 18], -22, 218)
# 4 归并
class Solution:
    prefixsum = []

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def merge(left, right, lower, upper):
            if right - left == 1:
                return 0
            mid = (left + right) // 2
            lo, up = mid, mid
            i = left
            cnt = 0
            cnt += merge(left, mid, lower, upper)
            cnt += merge(mid, right, lower, upper)
            while i < mid:
                while lo < right and self.prefixsum[lo] - self.prefixsum[i] < lower:
                    lo += 1
                while up < right and self.prefixsum[up] - self.prefixsum[i] <= upper:
                    up += 1
                cnt += up - lo
                i += 1
            merge_sort(left, mid, right)
            return cnt

        def merge_sort(left, mid, right):
            m = []
            l, r = left, mid
            while l < mid and r < right:
                if self.prefixsum[l] < self.prefixsum[r]:
                    m.append(self.prefixsum[l])
                    l += 1
                else:
                    m.append(self.prefixsum[r])
                    r += 1
            if l < mid:
                m.extend(self.prefixsum[l:mid])
            if r < right:
                m.extend(self.prefixsum[r:right])
            self.prefixsum[left:right] = m[:]

        self.prefixsum = [0, *itertools.accumulate(nums)]
        return merge(0, len(self.prefixsum), lower, upper)


Solution().countRangeSum([9, 3, 8, 19, 23, 22, 18], -22, 218)
