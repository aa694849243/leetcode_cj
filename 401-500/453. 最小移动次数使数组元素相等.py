'''给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动将会使 n - 1 个元素增加 1。

 

示例:

输入:
[1,2,3]

输出:
3

解释:
只需要3次移动（注意每次移动会增加两个元素的值）：

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/solution/zui-xiao-yi-dong-ci-shu-shi-shu-zu-yuan-su-xiang-d/
# 1 排序法 正向
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(len(nums) - 1, 0, -1):
            diff = nums[i] - nums[0]  # 每次将最低值增加diff达到最高值
            moves += diff
        return moves


# 2 数学 反向
# 其他值增加1，相当于本底值减1，那么将所有的其他值减少到最低值即可
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mi = min(nums)
        moves = 0
        for num in nums:
            moves += num - mi
        return moves


# 3动态规划
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        flag = nums[0]
        for num in nums[1:]:
            num += moves
            moves += num - flag
            flag = num
        return moves
