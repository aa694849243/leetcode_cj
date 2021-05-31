# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
#
#  由于答案可能很大，因此 返回答案模 10^9 + 7 。
#
#
#
#  示例 1：
#
#
# 输入：arr = [3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
#
#  示例 2：
#
#
# 输入：arr = [11,81,94,43,3]
# 输出：444
#
#
#
#
#  提示：
#
#
#  1 <= arr.length <= 3 * 104
#  1 <= arr[i] <= 3 * 104
#
#
#
#  Related Topics 栈 数组
#  👍 228 👎 0

from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        stack = []
        ans = 0
        for i, val in enumerate(arr):
            if not stack:
                stack.append([val, 1, val % mod])
            elif stack[-1][0] < val:
                stack.append([val, 1, (val + stack[-1][2]) % mod])
            else:
                a = 1
                while stack and stack[-1][0] >= val:
                    a += stack.pop()[1]
                if stack:
                    stack.append([val, a, (a * val + stack[-1][2]) % mod])
                else:
                    stack.append([val, a, a * val % mod])
            ans += stack[-1][2]
        return ans % mod


Solution().sumSubarrayMins([11, 81, 94, 43, 3])
