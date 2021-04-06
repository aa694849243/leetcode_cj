'''给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
 

提示：

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

import collections


# 1深度优先搜索
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        a = sum(nums)
        if a // k != a / k:
            return False
        eqal = a // k
        if max(nums) > eqal:
            return False
        nums.sort()

        def dfs(nums):
            if not nums:
                return True
            for i, x in enumerate(groups):
                a = nums.pop()
                if x + a <= eqal:
                    groups[i] += a
                    if dfs(nums):
                        return True
                    groups[i] -= a
                nums.append(a)
            return False

        while nums and nums[-1] == eqal:
            nums.pop()
            k -= 1
        groups = [0] * k
        return dfs(nums)


# 2深度优先搜索+状态压缩
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem or max(nums) > target:
            return False
        m = [None] * (1 << len(nums))
        m[-1] = True

        def sc(used, rem):
            if m[used] == None:
                flag = (rem - 1) % target + 1  # 保留1倍整数
                m[used] = any(sc(used | (1 << i), rem - nums[i]) for i in range(len(nums)) if used & (1 << i) == 0 and nums[i] <= flag)
            return m[used]

        return sc(0, sum(nums))


Solution().canPartitionKSubsets([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6], 3)
