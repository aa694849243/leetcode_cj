# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
#
#  对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
#
#  你可以返回任何满足上述条件的数组作为答案。
#
#
#
#  示例：
#
#  输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#
#
#
#
#  提示：
#
#
#  2 <= A.length <= 20000
#  A.length % 2 == 0
#  0 <= A[i] <= 1000
#
#
#
#  Related Topics 排序 数组
#  👍 203 👎 0

from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        odd, even = 1, 0
        for num in nums:
            if num % 2:
                ans[odd] = num
                odd += 2
            else:
                ans[even] = num
                even += 2
        return ans


# 原地修改
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2:
                while nums[odd] % 2:
                    odd += 2
                nums[i], nums[odd] = nums[odd], nums[i]
        return nums
