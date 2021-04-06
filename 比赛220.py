# https://leetcode-cn.com/contest/weekly-contest-220/ranking/
# 1
class Solution:

    def reformatNumber(self, number: str) -> str:
        tmp = ''
        ans = []
        for num in number:
            if num == ' ' or num == '-':
                continue
            else:
                tmp += num
                if len(tmp) == 3:
                    ans.append(tmp)
                    tmp = ''
        if tmp:
            ans.append(tmp)
        if len(ans) < 1:
            return ''
        elif len(ans) == 1:
            return ans[0]
        if len(ans[-1]) == 1:
            a = ans.pop()
            b = ans.pop()
            c = b + a
            ans.append(c[:2])
            ans.append(c[2:])
        return '-'.join(ans)


# 大神解法
class Solution:
    def reformatNumber(self, s: str) -> str:
        ans = []
        s = s.replace(' ', '').replace('-', '')
        while len(s) > 4:
            ans.append(s[:3])
            s = s[3:]
        if len(s) == 4:
            ans.append(s[:2])
            ans.append(s[2:])
        elif len(s) <= 3:
            ans.append(s)

        return "-".join(ans)


Solution().reformatNumber("1-23-45 6")

# 5630. 删除子数组的最大得分
import collections
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        m = {}
        l = 0
        m[nums[0]] = 0
        r = 1
        ans = 0
        while r < len(nums):
            if nums[r] in m:
                ans = max(sum(nums[l:r]), ans)
                for num in nums[l:m[nums[r]]]:
                    m.pop(num)
                l = m[nums[r]] + 1

            m[nums[r]] = r
            r += 1
        ans = max(sum(nums[l:r]), ans)
        return ans


# 大神解法
class Solution(object):
    def maximumUniqueSubarray(self, A):
        N = len(A)
        P = [0]
        for x in A: P.append(P[-1] + x)
        import collections
        count = collections.Counter()
        ans = i = 0
        for j, x in enumerate(A):
            count[x] += 1
            while count[x] >= 2:
                count[A[i]] -= 1
                i += 1
            ans = max(ans, P[j + 1] - P[i])
        return ans


Solution().maximumUniqueSubarray([4, 5, 8, 7, 7, 5, 3, 4, 56])

# 5631. 跳跃游戏 VI
import functools

import heapq


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        ma = dp[0]
        for i in range(1, len(nums)):
            if i < k:
                dp[i] = ma + nums[i]
                ma = max(ma, dp[i])
            else:
                dp[i] = ma + nums[i]
                ma = max(ma, dp[i])
                if dp[i - k] == ma:
                    ma = max(dp[i - k + 1:i + 1])
        return dp[-1]


# 大神解法
class MMQueue:
    def __init__(self):
        self.maq = collections.deque()
        self.len = 0

    def enqueue(self, v):
        self.len += 1

        c = 1
        while self.maq and self.maq[-1][0] < v:
            c += self.maq.pop()[1]
        self.maq.append([v, c])

    def dequeue(self):
        self.len -= 1

        self.maq[0][1] -= 1
        if self.maq[0][1] <= 0:
            self.maq.popleft()

    def max(self):
        return self.maq[0][0] if self.maq else 0

    def __len__(self):
        return self.len


class Solution:
    def maxResult(self, A: List[int], K: int) -> int:
        N = len(A)
        mq = MMQueue()
        mq.enqueue(A[0])
        ans = A[0]
        for i in range(1, N):
            if len(mq) > K:
                mq.dequeue()
            ans = A[i] + mq.max()
            mq.enqueue(ans)
        return ans


Solution().maxResult([1, -1, -2, 4, -7, 3], 2)
