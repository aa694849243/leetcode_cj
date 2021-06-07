# -*- coding: utf-8 -*-
import collections
import heapq
from typing import List


# 我们有一个项的集合，其中第 i 项的值为 values[i]，标签为 labels[i]。
#
#  我们从这些项中选出一个子集 S，这样一来：
#
#
#  |S| <= num_wanted
#  对于任意的标签 L，子集 S 中标签为 L 的项的数目总满足 <= use_limit。
#
#
#  返回子集 S 的最大可能的 和。
#
#
#
#  示例 1：
#
#  输入：values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
# 输出：9
# 解释：选出的子集是第一项，第三项和第五项。
#
#
#  示例 2：
#
#  输入：values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
# 输出：12
# 解释：选出的子集是第一项，第二项和第三项。
#
#
#  示例 3：
#
#  输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
# 输出：16
# 解释：选出的子集是第一项和第四项。
#
#
#  示例 4：
#
#  输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2
# 输出：24
# 解释：选出的子集是第一项，第二项和第四项。
#
#
#
#
#  提示：
#
#
#  1 <= values.length == labels.length <= 20000
#  0 <= values[i], labels[i] <= 20000
#  1 <= num_wanted, use_limit <= values.length
#
#  Related Topics 贪心算法 哈希表
#  👍 16 👎 0


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        q = []
        for i, val in enumerate(values):
            heapq.heappush(q, (-val, labels[i]))
        m = collections.defaultdict(int)
        ans = 0
        for _ in range(num_wanted):
            while q and m[q[0][1]] >= use_limit:
                heapq.heappop(q)
            if not q:
                break
            num, label = heapq.heappop(q)
            ans += num
            m[label] += 1
        return -ans


Solution().largestValsFromLabels([9,8,8,7,6],[0, 0, 0, 1, 1], 3, 1)
