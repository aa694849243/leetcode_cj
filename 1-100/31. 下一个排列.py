'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'字典序的意思是，假如把位置转换为数字，最后组合起来的数字，比如[1,3,7,9]字典序为1379'


class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                lo, hi = i, len(nums)
                while lo < hi:
                    mid = (lo + hi) // 2
                    if nums[mid] > nums[i-1]:
                        lo = mid + 1
                    else:
                        hi = mid
                lo -= 1
                nums[i - 1], nums[lo] = nums[lo], nums[i - 1]
                hi = len(nums) - 1
                while i < hi:
                    nums[i], nums[hi] = nums[hi], nums[i]
                    hi -= 1
                    i += 1
                return
        nums.reverse()
        return


nums = [1,1,5]
Solution().nextPermutation(nums)
1276531
