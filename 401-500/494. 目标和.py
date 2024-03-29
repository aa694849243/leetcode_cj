'''给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

 

示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
 

提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 ss 。
保证返回的最终结果能被 32 位整数存下。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

#0-1背包问题
# https://leetcode-cn.com/problems/target-sum/solution/494-mu-biao-he-dong-tai-gui-hua-zhi-01be-78ll/
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if S > sum(nums) or S < -sum(nums):
            return 0
        S = -S if S < 0 else S
        p = (sum(nums) + S)
        if p % 2:
            return 0
        p //= 2
        dp = [1] + [0] * p
        for num in nums:
            for target in range(p, num - 1, -1):
                dp[target] += dp[target - num]
        return dp[p]


a = [1000]
b = 1000
Solution().findTargetSumWays(a, b)
