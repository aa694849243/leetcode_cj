'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def threeSumClosest(nums: list, target: int) -> int:
    nums.sort()
    diff = float('inf')
    s = {}
    s[diff] = diff
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            i_ = nums[left] + nums[right] + nums[i]
            if i_ == target:
                return i_
            elif i_ < target:
                diff = min(abs(target - i_), diff)
                s[diff] = i_ if diff == abs(target - i_) else s[diff]
                left += 1
            else:
                diff = min(abs(target - i_), diff)
                s[diff] = i_ if diff == abs(target - i_) else s[diff]
                right -= 1
    return s[diff]


nums = [-1, 2, 1, -4]
nums = [0, 0, 0]
nums = [1, 1, -1, -1, 3]
nums = [1, 2, 4, 8, 16, 32, 64, 128]
target = 1
nums = [0, 2, 1, -3]
threeSumClosest(nums, target)
