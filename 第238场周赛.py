# 5738. K 进制表示下的各位数字总和
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        li = []
        while n > 0:
            li.append(n % k)
            n //= k
        return sum(li)


Solution().sumBase(216, 6)
# 5739. 最高频元素的频数
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1
        nums.sort()
        ans = 1
        dp = [0] * len(nums)
        dp[0] = 0
        l = 0
        for i, val in enumerate(nums[1:], 1):
            if dp[i - 1] + (val - nums[i - 1]) * (i - l) <= k:
                ans = max(ans, i - l + 1)
                dp[i] = dp[i - 1] + (val - nums[i - 1]) * (i - l)
            else:
                a = dp[i - 1]
                while a + (val - nums[i - 1]) * (i - l) > k:
                    a -= (nums[i - 1] - nums[l])
                    l += 1
                dp[i] = a + (val - nums[i - 1]) * (i - l)
                ans = max(ans, i - l + 1)
        return ans


# 5740. 所有元音按顺序排布的最长子字符串
import collections


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        m = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        m2 = collections.defaultdict(int)
        dp = [0] * len(word)
        cmp = 0
        cmp |= (1 << (m[word[0]]))
        dp[0] = cmp
        l = 0
        ans = 0
        for i in range(len(word)):
            m2[word[i]] += 1
            cmp = dp[i - 1]
            cmp |= (1 << m[word[i]])
            if cmp == 31 and word[i] >= word[i - 1]:
                ans = max(ans, i - l + 1)
                dp[i] = cmp
            elif word[i] >= word[i - 1]:
                dp[i] = dp[i - 1] | (1 << m[word[i]])
            else:
                dp[i] = 0 | (1 << m[word[i]])
                l = i

        return ans


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1
        restrictions = [[1, 0]] + restrictions
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
        restrictions.sort()
        ans = 0
        res_r = [(1, 0)]
        for x, y in restrictions[1:]:
            a = min(y, x - res_r[-1][0] + res_r[-1][1])
            res_r.append((x, a))
        for i in range(len(res_r) - 2, -1, -1):
            x, y = res_r[i]
            a = min(y, res_r[i + 1][0] - x + res_r[i + 1][1])
            res_r[i] = (x, a)
        for i, (x, y) in enumerate(res_r[1:], 1):
            x_, y_ = res_r[i - 1]
            h = ((x - y) - (x_ - y_)) // 2 + y
            ans = max(ans, h)
        return ans


Solution().maxBuilding(100, [[65, 42], [96, 0], [35, 46]])
