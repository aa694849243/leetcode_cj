"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。


请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

 

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# ------------------------------------caojie-------------删除法----------------------------------------------
def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    m, n = len(nums1), len(nums2)
    while m > 0 and n > 0:
        if nums1[0] <= nums2[0]:
            mid1 = nums1.pop(0)
            m -= 1
        else:
            mid1 = nums2.pop(0)
            n -= 1
        # 弹出最小值，mid保存这一步的弹出值
        if m > 0 and n > 0:
            if nums1[-1] <= nums2[-1]:
                mid2 = nums2.pop()
                n -= 1
            else:
                mid2 = nums1.pop()
                m -= 1
        # 弹出最大值
        elif m > 0:
            mid2 = nums1.pop()
            m -= 1
        elif n > 0:
            mid2 = nums2.pop()
            n -= 1
        # 出现一个数组为空时，则弹出另一个数组的最大值，并用mid2保存
    if n > 0:
        mid = nums2[n // 2] if n % 2 == 1 else (nums2[n // 2 - 1] + nums2[n // 2]) / 2
        return mid
    # 只剩n数组的情况
    if m > 0:
        mid = nums1[m // 2] if m % 2 == 1 else (nums1[m // 2 - 1] + nums1[m // 2]) / 2
        return mid
    # 只剩m数组的情况
    mid = (mid1 + mid2) / 2  # 上一步已经全部弹出，则将保留的mid1和mid2使用
    return mid


# ---------------------------------------二分法-------------------------------------------------------------
def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    n, m = len(nums1), len(nums2)
    MID = (n + m - 1) // 2
    left = 0
    right = n - 1
    mid1 = (left + right) // 2
    mid2 = MID - mid1
    if n == 0:
        mid_left = nums2[m // 2] if m % 2 == 1 else 0.5 * (nums2[m // 2] + nums2[m // 2] - 1)
        return mid_left
    while left < right:
        if nums1[mid1] > nums2[mid2]:
            right = mid1 - 1
            if right < 0:  # 这一步防止mid1=0时对应的数比较大，此时mid1就不用往回找了，此时mid位置就是最终位置
                break
        elif nums1[mid1] < nums2[mid2]:
            left = mid1 + 1
            if left > n:  # 此时mid1在右端点，mid1也不用再找了，mid1对应最终位置
                break
        else:
            return nums1[mid1]
        mid1 = (left + right) // 2
        mid2 = MID - mid1
    if nums1[mid1] == nums2[mid2]:
        return nums1[mid1]
    if nums1[mid1] < nums2[mid2]:
        if mid2 - 1 >= 0:
            mid_left = max(nums1[mid1], nums2[mid2 - 1])
            # 第一种情况
        else:
            mid_left = nums1[mid1]
            # 第二种情况
    if nums1[mid1] > nums2[mid2]:
        if mid1 - 1 >= 0:
            mid_left = max(nums1[mid1 - 1], nums2[mid2])
            # 第三种情况
        else:
            mid_left = nums2[mid2]
            # 第四种情况
    if (n + m) % 2 == 1:
        return mid_left  # 奇数只返回mid_left
    if nums1[mid1] < nums2[mid2]:
        if mid1 + 1 <= n - 1:
            mid_right = min(nums1[mid1 + 1], nums2[mid2])
        else:
            mid_right = nums2[mid2]
    if nums1[mid1] > nums2[mid2]:
        if mid2 + 1 <= m - 1:
            mid_right = min(nums1[mid1], nums2[mid2 + 1])
            # 第三种情况
        else:
            mid_right = nums1[mid1]
    return (mid_left + mid_right) / 2


'''
n+m为奇数只需要考虑mid_left
nums1[mid1]<nums2[mid2]
第一种情况
nums1   1   15|  18    19
            mid1
nums2   4   5   |16    7    
                mid2
                
mid1+1或mid2-1不存在的情况
nums1   1   2   3|
                mid1
nums2   |4   5   6 
        mid2
'''

'''
nums1[mid1]>nums[mid2]
第三种情况
nums1   1  |8  16  32
           mid1
nums2   3   4  7|  19
               mid2                
mid1-1或mid2+1不存在的情况
nums1   |4   5   6
        mid1    
nums2   1   2   3|
                mid2
'''

nums1 = [3, 4]
nums2 = [1, 2]
findMedianSortedArrays(nums1, nums2)
a=1