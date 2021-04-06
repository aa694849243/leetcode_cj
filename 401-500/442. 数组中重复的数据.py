'''给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 索引法 enumerate参数
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]:  # 每次将nums[i]上的数送到正确的位置上，若正确的位置上已经存在正确的数则跳出循环 nums[x-1]==x则x在正确的位置上
                tmp = nums[i]
                loc = nums[i] - 1  # nums[i]-1为nums[i]的正确位置
                nums[i] = nums[nums[i] - 1]
                nums[loc] = tmp
        res = []
        for i, j in enumerate(nums, 1):
            if i != j:
                res.append(j)
        return res


# 奇偶法
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                res.append(abs(nums[i]))
            nums[abs(nums[i]) - 1] *= -1
        return res


Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
