'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# 贪心法---参考官方-----------------------------------------------------------------------------------------------------
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:  # 当i小于最大边界值时继续前进
                maxPos = max(maxPos, i + nums[i])  # 更新最大边界值
                if i == end:  # end保留边界上一步的边界值，当i到达上一步的边界值时更新最新的end即目前最大的边界值
                    end = maxPos
                    step += 1  # 到达一次end，步数+1
        return step


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 参考官方后caojie版本
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = len(nums) - 1
        count = 0
        start = 0
        maxborder = nums[start]
        s = {}
        if maxborder >= end:  # 一步就能到达边界的情况
            return 1 if len(nums) != 1 else 0
        while start < end:
            count += 1  # 走一步，试探情况
            for i in range(1, nums[start] + 1):
                border = start + i + nums[start + i]
                maxborder = max(border, maxborder)
                if maxborder >= end:
                    count += 1
                    return count
                if maxborder == border:
                    s['maxborder'] = i
            start += s['maxborder']


nums = [2, 3, 1, 4, 1, 1, 1]
Solution().jump(nums)
