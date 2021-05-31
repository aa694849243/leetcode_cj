import bisect
import collections, heapq, itertools
from typing import List


# 给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i
# + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。
#
#
#
#  示例 1：
#
#
# 输入：arr = [3,1,3,6]
# 输出：false
#
#
#  示例 2：
#
#
# 输入：arr = [2,1,2,6]
# 输出：false
#
#
#  示例 3：
#
#
# 输入：arr = [4,-2,2,-4]
# 输出：true
# 解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
#
#
#  示例 4：
#
#
# 输入：arr = [1,2,4,16,8,4]
# 输出：false
#
#
#
#
#  提示：
#
#
#  0 <= arr.length <= 3 * 104
#  arr.length 是偶数
#  -105 <= arr[i] <= 105
#
#  Related Topics 数组 哈希表
#  👍 49 👎 0


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        def solve(arr):
            m = collections.Counter(arr)
            for key in sorted(m.keys()):
                if m[2 * key] < m[key]:
                    return False
                if not m[key]:
                    continue
                m[2 * key] -= m[key]
                m[key] = 0
            return True
        if not arr:
            return True

        arr.sort()
        if arr[0] >= 0:
            return solve(arr)
        flag = bisect.bisect_left(arr, 0)
        a1, a2 = arr[:flag], arr[flag:]
        if len(a1) % 2 or len(a2) % 2:
            return False
        a1 = list(map(lambda x: x * -1, a1))
        return solve(a1) and solve(a2)


Solution().canReorderDoubled([4, -2, 2, -4])
