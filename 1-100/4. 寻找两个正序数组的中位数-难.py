# log(n+m)解法
# https://leetcode.cn/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_k_element(k):
            idx1, idx2 = 0, 0
            while 1:
                if idx1 == m:
                    return nums2[idx2 + k - 1]
                elif idx2 == n:
                    return nums1[idx1 + k - 1]
                elif k == 1:
                    return min(nums1[idx1], nums2[idx2])
                new_idx1, new_idx2 = min(idx1 + k // 2 - 1, len(nums1) - 1), min(idx2 + k // 2 - 1, len(nums2) - 1) # 每次每边缩减一半，可以保证不每次减去的数都真正应该被减去
                if nums1[new_idx1] <= nums2[new_idx2]:
                    k -= new_idx1 - idx1 + 1
                    idx1 = new_idx1 + 1
                else:
                    k -= new_idx2 - idx2 + 1
                    idx2 = new_idx2 + 1

        m, n = len(nums1), len(nums2)
        total = m + n
        if total % 2:
            return get_k_element(total // 2 + 1)
        else:
            return (get_k_element(total // 2) + get_k_element(total // 2 + 1)) / 2


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().findMedianSortedArrays([2], [])
)
