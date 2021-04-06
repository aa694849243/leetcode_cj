'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# ------------------------------双指针+排序--------------------------------------------------------------------------------
def threeSum(nums: list):
    if len(nums) < 3:
        return []
    nums.sort()
    ans = []
    i = 0
    while i <= len(nums) - 3:
        diff = -nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            a = nums[left] + nums[right]
            if a == diff:
                t = [nums[i], nums[left], nums[right]]
                ans.append(t)
                while left + 1 < right and nums[left] == nums[left + 1]:
                    left += 1
                while right - 1 > left and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
                continue
            elif a > diff:
                right -= 1
                continue
            else:
                left += 1
                continue
        while i + 1 <= len(nums) - 3 and nums[i + 1] == nums[i]:
            i += 1
        i += 1
    return ans


nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0]
threeSum(nums)
