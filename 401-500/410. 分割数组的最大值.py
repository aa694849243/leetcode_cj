'''给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-largest-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1 动态规划
# 超时
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        sub = [0]
        dp = [[float('inf')] * (m + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 0
        for num in nums:
            sub.append(sub[-1] + num)
        for i in range(1, len(nums) + 1):
            for j in range(1, min(m, i) + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sub[i] - sub[k]))
        return dp[-1][-1]


# 2 二分法 最小最大问题 最大最小问题
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(val):
            cnt = 1
            cum = 0
            for num in nums:
                if cum + num > val:
                    cum = num
                    cnt += 1
                else:
                    cum += num
            return cnt <= m

        left = max(nums)
        right = sum(nums) + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


nums = [7, 2, 5, 10, 8]
m = 2
Solution().splitArray(nums, m)
