# -*- coding: utf-8 -*-
# 给你一个下标从 0 开始的整数数组 arr 和一个整数 k 。数组 arr 是一个循环数组。换句话说，数组中的最后一个元素的下一个元素是数组中的第一个元素，
# 数组中第一个元素的前一个元素是数组中的最后一个元素。
#
#  你可以执行下述运算任意次：
#
#
#  选中 arr 中任意一个元素，并使其值加上 1 或减去 1 。
#
#
#  执行运算使每个长度为 k 的 子数组 的元素总和都相等，返回所需要的最少运算次数。
#
#  子数组 是数组的一个连续部分。
#
#
#
#  示例 1：
#
#  输入：arr = [1,4,1,3], k = 2
# 输出：1
# 解释：在下标为 1 的元素那里执行一次运算，使其等于 3 。
# 执行运算后，数组变为 [1,3,1,3] 。
# - 0 处起始的子数组为 [1, 3] ，元素总和为 4
# - 1 处起始的子数组为 [3, 1] ，元素总和为 4
# - 2 处起始的子数组为 [1, 3] ，元素总和为 4
# - 3 处起始的子数组为 [3, 1] ，元素总和为 4
#
#
#  示例 2：
#
#  输入：arr = [2,5,5,7], k = 3
# 输出：5
# 解释：在下标为 0 的元素那里执行三次运算，使其等于 5 。在下标为 3 的元素那里执行两次运算，使其等于 5 。
# 执行运算后，数组变为 [5,5,5,5] 。
# - 0 处起始的子数组为 [5, 5, 5] ，元素总和为 15
# - 1 处起始的子数组为 [5, 5, 5] ，元素总和为 15
# - 2 处起始的子数组为 [5, 5, 5] ，元素总和为 15
# - 3 处起始的子数组为 [5, 5, 5] ，元素总和为 15
#
#
#
#
#  提示：
#
#
#  1 <= k <= arr.length <= 10⁵
#  1 <= arr[i] <= 10⁹
#
#
#  Related Topics 数组 数学 数论 排序
#  👍 21 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        t = gcd(len(arr), k)
        ans = 0
        for i in range(t):
            tmp = sorted(arr[i::t])
            mid= len(tmp) // 2
            ans+= tmp[mid]*mid-sum(tmp[:mid])+sum(tmp[mid+1:])-tmp[mid]*(len(tmp)-mid-1)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
