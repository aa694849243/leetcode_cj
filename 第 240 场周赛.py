import collections
import heapq
import bisect
import math
import itertools
# 5750. 人口最多的年份
from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        m = collections.defaultdict(int)
        for l, r in logs:
            for i in range(l, r):
                m[i] += 1
        ans = 0
        ma = 0

        for y in sorted(m.keys()):
            if m[y] > ma:
                ans = y
                ma = m[y]
        return ans


# 5751. 下标对中的最大距离
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        stack1 = []
        for i, num in enumerate(nums1):
            if not stack1 or num < stack1[-1][1]:
                stack1.append((i, num))
        stack2 = []
        for i, num in enumerate(nums2[::-1]):
            if not stack2:
                stack2.append(num)
            else:
                stack2.append(max(stack2[-1], num))
        n = len(nums2) - 1
        for i, num in stack1:
            x = bisect.bisect_left(stack2, num)
            if x == n + 1:
                continue
            j = n - x
            ans = max(ans, j - i)

        return ans


# 5752. 子数组最小乘积的最大值
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        LR = {}
        sums = [0]
        for i in nums:
            sums.append(sums[-1] + i)
        res = 0
        for i, n in sorted(enumerate(nums), key=lambda x: x[1], reverse=True):
            L = LR.get(i, i)
            R = LR.get(i + 1, i + 1)
            LR[L] = R
            LR[R] = L
            res = max(res, n * (sums[R] - sums[L]))
        return res % (10 ** 9 + 7)


# 5751. 下标对中的最大距离
# 双单调栈
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        cum = [0] + [*itertools.accumulate(nums)]
        n = len(nums)
        stack = []
        left = []
        for i, val in enumerate(nums):
            if stack:
                while stack and val < stack[-1][1]:
                    stack.pop()
            if not stack:
                left.append(0)
            else:
                left.append(stack[-1][0] + 1)
            stack.append((i, val))
        stack.clear()
        right = []
        for i in range(len(nums) - 1, -1, -1):
            if stack:
                while stack and nums[i] <= stack[-1][1]:
                    stack.pop()
            if not stack:
                right.append(n)
            else:
                right.append(stack[-1][0])
            stack.append((i, nums[i]))
        right = right[::-1]
        ans = 0
        for i, val in enumerate(nums):
            ans = max(ans, val * (cum[right[i]] - cum[left[i]]))
        return ans % mod


# LR法
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod=10**9+7
        LR = {}
        cum = [0] + [*itertools.accumulate(nums)]
        ans=0
        for i, val in sorted(enumerate(nums), key=lambda x: x[1], reverse=True):
            l = LR.get(i, i)
            r = LR.get(i + 1, i + 1)
            LR[r] = l
            LR[l] = r
            ans=max(ans,val*(cum[r]-cum[l]))
        return ans%mod


Solution().maxSumMinProduct([2, 3, 3, 1, 2])
