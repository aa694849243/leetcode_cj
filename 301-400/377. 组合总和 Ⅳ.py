'''给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。
进阶：
如果给定的数组中含有负数会怎么样？
问题会产生什么变化？
我们需要在题目中添加什么限制来允许负数的出现？

致谢：
特别感谢 @pbrother 添加此问题并创建所有测试用例。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 背包问题 组合问题 完全背包
# 递归 超时
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        def rec(nums, target):
            if target == 0:
                return 1
            if nums[0] > target:
                return 0
            if nums[0] == target:
                return 1
            m = 0
            for i in range(len(nums)):
                m += rec(nums, target - nums[i])
            return m

        return rec(nums, target)


# 动态规划
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # 当目标值i==num时，表示有一个组合符合要求
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num] #dp[i-num]表示当最后一个选择num时之前的组合总数，此时选择num刚好等于最终值
        return dp[-1]


a = [1, 2, 3]
b = 4

Solution().combinationSum4(a, b)

# 对于进阶问题的思考
# 1、如果给定的数组中含有负数会怎么样？问题会产生什么变化？
#
# 如果有负数，相当于给定数组中的元素有了更多的组合，特别是出现了一对相反数的时候，例如题目中的示例 [-4, 1, 2, 3, 4]，target = 4 的时候，-4 和 4 可以无限次地、成对添加到题目中的示例中，成为新的组合，那么这道问题就没有什么意义了。
#
# 仔细思考，负数我只要不选它就行了。但由于这道问题的问法是“组合”，因此我们要保证有负数参与进来，不能够与已有的正数的组合之和为 0 即可。
#
# 2、我们需要在题目中添加什么限制来允许负数的出现？
#
# 如果有负数参与进来，不能够与已有的正数的组合之和为 0 ；
# 或者限制负数的使用次数，设计成类似 0-1 背包问题的样子。
# 可能有考虑不完全的地方，欢迎讨论。
#
# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/combination-sum-iv/solution/dong-tai-gui-hua-python-dai-ma-by-liweiwei1419/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
