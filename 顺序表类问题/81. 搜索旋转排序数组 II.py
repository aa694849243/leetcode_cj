'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] >= nums[right]:
                if nums[left] < target < nums[right]:
                    return False
                elif nums[left] == target or nums[right] == target:
                    return True
                else:
                    left += 1
                    right -= 1
            else:
                right += 1
                while left<right:
                    mid=(left+right)//2
                    if nums[mid]<target:
                        left=mid+1
                    elif nums[mid]>target:
                        right=mid
                    else:
                        return True
                return False
        return False
#寻找旋转点的做法
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left = 0
        right = len(nums) - 1
        while left <= right:
            # print(left, right)
            mid = left + (right - left) // 2
            # 等于目标值
            if nums[mid] == target: return True

            if nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
            # 在前部分
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


# 作者：powcai
# 链接：https: // leetcode - cn.com / problems / search - in -rotated - sorted - array - ii / solution / er - fen - by - powcai /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。