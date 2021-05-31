import collections, heapq, itertools
from typing import List


# 给定一个由不同正整数的组成的非空数组 A，考虑下面的图：
#
#
#  有 A.length 个节点，按从 A[0] 到 A[A.length - 1] 标记；
#  只有当 A[i] 和 A[j] 共用一个大于 1 的公因数时，A[i] 和 A[j] 之间才有一条边。
#
#
#  返回图中最大连通组件的大小。
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：[4,6,15,35]
# 输出：4
#
#
#
#  示例 2：
#
#
# 输入：[20,50,9,63]
# 输出：2
#
#
#
#  示例 3：
#
#
# 输入：[2,3,6,7,4,12,21,39]
# 输出：8
#
#
#
#
#
#  提示：
#
#
#  1 <= A.length <= 20000
#  1 <= A[i] <= 100000
#
#  Related Topics 并查集 数学
#  👍 50 👎 0


# 设W = max(A[i])
# W = max(A[i])，R =√W
# R = W。对于数组A中的每个数，最多只有一个非本身的质因数p满足p≥R。这就意味着最多只有R + A.length"
# R + A.length个不同的质因数：为本身的质因数最多有A.length"
# A.length个，非本身的质因数一定比R小，最多有R个。
# 时间复杂度：O(N√W)，其中N是A的长度，W=max(A[i])
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        if 1 in nums:
            nums.remove(1)
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            a = find(x)
            b = find(y)
            if a != b:
                f[b] = a

        li = []
        for num in nums:
            a = set()
            for factor in range(2, int(num ** .5) + 1):
                if num % factor == 0:
                    a.add(factor)
                    a.add(num//factor)
            a.add(num)
            li.append(list(a))
        for a in li:
            for num in a:
                union(a[0], num)
        coun=collections.defaultdict(int)
        for a in li:
            coun[find(a[0])]+=1
        return max(coun.values())
Solution().largestComponentSize([4,6,15,35])