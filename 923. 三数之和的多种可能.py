# 给定一个整数数组 A，以及一个整数 target 作为目标值，返回满足 i < j < k 且 A[i] + A[j] + A[k] == target 的
# 元组 i, j, k 的数量。
#
#  由于结果会非常大，请返回 结果除以 10^9 + 7 的余数。
#
#
#
#  示例 1：
#
#  输入：A = [1,1,2,2,3,3,4,4,5,5], target = 8
# 输出：20
# 解释：
# 按值枚举（A[i]，A[j]，A[k]）：
# (1, 2, 5) 出现 8 次；
# (1, 3, 4) 出现 8 次；
# (2, 2, 4) 出现 2 次；
# (2, 3, 3) 出现 2 次。
#
#
#  示例 2：
#
#  输入：A = [1,1,2,2,2,2], target = 5
# 输出：12
# 解释：
# A[i] = 1，A[j] = A[k] = 2 出现 12 次：
# 我们从 [1,1] 中选择一个 1，有 2 种情况，
# 从 [2,2,2,2] 中选出两个 2，有 6 种情况。
#
#
#
#
#  提示：
#
#
#  3 <= A.length <= 3000
#  0 <= A[i] <= 100
#  0 <= target <= 300
#
#  Related Topics 双指针
#  👍 72 👎 0

from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        mod = 10 ** 9 + 7
        ans = 0

        def cal(l, r):
            if arr[l] == arr[r]:
                return -1, -1, (r - l + 1) * (r - l) // 2
            left, right = 1, 1
            while arr[l + 1] == arr[l]:
                l += 1
                left += 1
            while arr[r - 1] == arr[r]:
                r -= 1
                right += 1
            return l + 1, r - 1, left * right

        for i, val in enumerate(arr[:-2]):
            t = target - val
            l, r = i + 1, len(arr) - 1
            while l < r:
                if arr[l] + arr[r] == t:
                    l, r, a = cal(l, r)
                    ans += a
                elif arr[l] + arr[r] < t:
                    l += 1
                else:
                    r -= 1
            ans %= mod

        return ans


Solution().threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8)
