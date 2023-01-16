# -*- coding: utf-8 -*-
# 给你一个整数数组 nums 和一个整数 threshold 。
#
#  找到长度为 k 的 nums 子数组，满足数组中 每个 元素都 大于 threshold / k 。
#
#  请你返回满足要求的 任意 子数组的 大小 。如果没有这样的子数组，返回 -1 。
#
#  子数组 是数组中一段连续非空的元素序列。
#
#
#
#  示例 1：
#
#  输入：nums = [1,3,4,3,1], threshold = 6
# 输出：3
# 解释：子数组 [3,4,3] 大小为 3 ，每个元素都大于 6 / 3 = 2 。
# 注意这是唯一合法的子数组。
#
#
#  示例 2：
#
#  输入：nums = [6,5,6,5,8], threshold = 7
# 输出：1
# 解释：子数组 [8] 大小为 1 ，且 8 > 7 / 1 = 7 。所以返回 1 。
# 注意子数组 [6,5] 大小为 2 ，每个元素都大于 7 / 2 = 3.5 。
# 类似的，子数组 [6,5,6] ，[6,5,6,5] ，[6,5,6,5,8] 都是符合条件的子数组。
# 所以返回 2, 3, 4 和 5 都可以。
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10⁵
#  1 <= nums[i], threshold <= 10⁹
#
#
#  Related Topics 栈 并查集 数组 单调栈
#  👍 27 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        cnts = []
        n = len(nums)
        for num in nums:
            cnts.append(threshold // num + 1)
        st = []
        lefts = [-1] * n
        rights = [n] * n
        for i, cnt in enumerate(cnts):
            while st and cnts[st[-1]] < cnt:
                rights[st.pop()] = i
            st.append(i)
        st = []
        for i in range(n - 1, -1, -1): # 波峰波谷逆序
            while st and cnts[st[-1]] < cnts[i]:
                lefts[st.pop()] = i
            st.append(i)
        for i in range(n):
            if rights[i] - lefts[i] - 1 >= cnts[i]:
                return cnts[i]
        return -1
# leetcode submit region end(Prohibit modification and deletion)
