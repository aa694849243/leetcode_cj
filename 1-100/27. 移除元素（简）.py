'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

 

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#----------------------双指针法-------------------------------------------------
def removeElement(nums, val) -> int:
    i, j = 0, 0
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            i += 1
            j += 1
        else:
            i += 1
    return j
#改良版双指针法-----43%---------------------当移除的元素很少时没必要复制，只需要将需要更改的元素与列表尾部元素交换即可
def removeElement(nums, val) -> int:
    i, j = 0, 0
    while i < len(nums)-j:
        if nums[i] == val:
            j += 1
            nums[i] = nums[-j]
        else:
            i += 1
    return len(nums)-j
