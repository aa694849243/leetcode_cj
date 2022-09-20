import collections, heapq, itertools
from typing import List
# 给你一个由 n 个正整数组成的数组 nums 。
#
#  你可以对数组的任意元素执行任意次数的两类操作：
#
#
#  如果元素是 偶数 ，除以 2
#
#
#
#  例如，如果数组是 [1,2,3,4] ，那么你可以对最后一个元素执行此操作，使其变成 [1,2,3,2]
#
#
#  如果元素是 奇数 ，乘上 2
#
#  例如，如果数组是 [1,2,3,4] ，那么你可以对第一个元素执行此操作，使其变成 [2,2,3,4]
#
#
#
#
#  数组的 偏移量 是数组中任意两个元素之间的 最大差值 。
#
#  返回数组在执行某些操作之后可以拥有的 最小偏移量 。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,3,4]
# 输出：1
# 解释：你可以将数组转换为 [1,2,3,2]，然后转换成 [2,2,3,2]，偏移量是 3 - 2 = 1
#
#
#  示例 2：
#
#
# 输入：nums = [4,1,5,20,3]
# 输出：3
# 解释：两次操作后，你可以将数组转换为 [4,2,5,5,3]，偏移量是 5 - 2 = 3
#
#
#  示例 3：
#
#
# 输入：nums = [2,10,8]
# 输出：3
#
#
#
#
#  提示：
#
#
#  n == nums.length
#  2 <= n <= 5 * 10⁹
#
#
#  Related Topics 贪心 数组 有序集合 堆（优先队列） 👍 73 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from sortedcontainers import SortedSet
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        lst = list(set(nums))
        for i, num in enumerate(lst):
            if num % 2:
                lst[i] = num * 2
        s = SortedSet(lst)
        res = s[-1] - s[0]
        while s[-1] % 2==0:
            res = min(res, s[-1] - s[0])
            a = s.pop()
            a //= 2
            s.add(a)
        res=min(res, s[-1] - s[0])
        return res

# leetcode submit region end(Prohibit modification and deletion)
Solution().minimumDeviation([1,2,3,4])