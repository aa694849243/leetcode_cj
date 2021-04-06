'''你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

 

示例 1：

输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出：[20,24]
解释：
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
示例 2：

输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
输出：[1,1]
示例 3：

输入：nums = [[10,10],[11,11]]
输出：[10,11]
示例 4：

输入：nums = [[10],[11]]
输出：[10,11]
示例 5：

输入：nums = [[1],[2],[3],[4],[5],[6],[7]]
输出：[1,7]
 

提示：

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] 按非递减顺序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
# 1堆
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        a = []
        xMax = float('-inf')
        p = 0
        for n, l in enumerate(nums):
            heapq.heappush(a, (l[0], p, n))
            xMax = max(xMax, l[0])
        xMin = a[0][0]
        bestl = xMin
        bestr = xMax
        while True:
            x, p, i = heapq.heappop(a)
            if p >= len(nums[i]) - 1:
                break
            heapq.heappush(a, (nums[i][p + 1], p + 1, i))
            xMax = max(nums[i][p + 1], xMax)
            xMin = a[0][0]
            bestl, bestr = [xMin, xMax] if xMax - xMin < bestr - bestl else [bestl, bestr]
        return [bestl, bestr]


# 2哈希表+滑动窗口
import collections


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        m = collections.defaultdict(list)
        for i, l in enumerate(nums):
            for num in l:
                m[num].append(i)
        xMin = min(m.keys())
        xMax = max(m.keys())
        l, r = xMin, xMin - 1
        bestl, bestr = xMin, xMax
        a = collections.defaultdict(int)
        while r < xMax:
            r += 1
            for loc in m[r]:
                a[loc] += 1
            if len(a.keys()) == len(nums):
                if r - l < bestr - bestl:
                    bestr, bestl = r, l
                while True:
                    for loc in m[l]:
                        a[loc] -= 1
                        if a[loc] == 0:
                            a.pop(loc)
                    l += 1
                    if len(a.keys()) != len(nums):
                        break
                    elif r - l < bestr - bestl:
                        bestr, bestl = r, l
        return [bestl, bestr]


Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
