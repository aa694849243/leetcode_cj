'''集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

 

示例 1：

输入：nums = [1,2,2,4]
输出：[2,3]
示例 2：

输入：nums = [1,1]
输出：[1,2]
 

提示：

2 <= nums.length <= 104
1 <= nums[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-mismatch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1不使用额外空间
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
                return ans


# 2位操作
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = 0
        for i in range(1, len(nums) + 1):
            a ^= (i ^ nums[i - 1])
        rightmostbit = a & -a
        xor1 = 0
        xor0 = 0
        for i in range(1, len(nums) + 1):
            if i & rightmostbit:
                xor1 ^= i
            else:
                xor0 ^= i
            if nums[i - 1] & rightmostbit:
                xor1 ^= nums[i - 1]
            else:
                xor0 ^= nums[i - 1]
        return [xor1, xor0] if xor1 in nums else [xor0, xor1]


Solution().findErrorNums([3, 2, 3, 4, 6, 5])
