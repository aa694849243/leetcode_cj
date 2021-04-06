'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#-----------------caojie--99%-------------------------------------------------------------------------
#二分法+双指针--https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/er-fen-fa-shuang-zhi-zhen-by-aa694849243/
class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        high = len(nums) - 1
        low = 0
        while low <= high:
            if nums[low] >= nums[high]:
                if nums[high] < target < nums[low]:
                    return -1
                elif nums[high] == target:
                    return high
                elif nums[low] == target:
                    return low
                low += 1
                high -= 1
            else:
                high += 1
                while low < high:
                    mid = (low + high) // 2
                    if target == nums[mid]:
                        return mid
                    elif target < nums[mid]:
                        high = mid
                    else:
                        low = mid + 1
                break
        return -1


nums = [1, 3]
target = 4
Solution().search(nums, target)
