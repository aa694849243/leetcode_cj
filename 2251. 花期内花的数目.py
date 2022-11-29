# -*- coding: utf-8 -*-
# 给你一个下标从 0 开始的二维整数数组 flowers ，其中 flowers[i] = [starti, endi] 表示第 i 朵花的 花期 从
# starti 到 endi （都 包含）。同时给你一个下标从 0 开始大小为 n 的整数数组 persons ，persons[i] 是第 i 个人来看花的时间。
#
#  请你返回一个大小为 n 的整数数组 answer ，其中 answer[i]是第 i 个人到达时在花期内花的 数目 。
#
#
#
#  示例 1：
#
#
#
#  输入：flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
# 输出：[1,2,2,2]
# 解释：上图展示了每朵花的花期时间，和每个人的到达时间。
# 对每个人，我们返回他们到达时在花期内花的数目。
#
#
#  示例 2：
#
#
#
#  输入：flowers = [[1,10],[3,3]], persons = [3,3,2]
# 输出：[2,2,1]
# 解释：上图展示了每朵花的花期时间，和每个人的到达时间。
# 对每个人，我们返回他们到达时在花期内花的数目。
#
#
#
#
#  提示：
#
#
#  1 <= flowers.length <= 5 * 10⁴
#  flowers[i].length == 2
#  1 <= starti <= endi <= 10⁹
#  1 <= persons.length <= 5 * 10⁴
#  1 <= persons[i] <= 10⁹
#
#
#  Related Topics 数组 哈希表 二分查找 有序集合 前缀和 排序
#  👍 36 👎 0

from typing import List
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        prefix = collections.defaultdict(int)
        for st, en in flowers:
            prefix[st] += 1
            prefix[en + 1] -= 1
        m = collections.defaultdict(list)
        for idx, num in enumerate(persons):
            m[num].append(idx)
        res = [0] * len(persons)
        cur_lst = sorted(m)
        cur = 0
        p_lst = sorted(prefix)
        cnt = 0
        for p in range(len(p_lst) - 1):
            cnt += prefix[p_lst[p]]
            while cur < len(cur_lst) and cur_lst[cur] < p_lst[p]:
                cur += 1
            if cur >= len(cur_lst):
                break
            while cur<len(cur_lst) and p_lst[p] <= cur_lst[cur] < p_lst[p + 1]:
                for idx in m[cur_lst[cur]]:
                    res[idx] = cnt
                cur += 1
            if cur >= len(cur_lst):
                break
        return res


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().fullBloomFlowers([[11, 11], [24, 46], [3, 25], [44, 46]], [1, 8, 26, 7, 43, 26, 1]))
