# -*- coding: utf-8 -*-
import collections
import heapq
from typing import List


# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
#
#
#  你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
#
#  返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
#
#
#
#  示例 1:
#
#  输入：s = "dcab", pairs = [[0,3],[1,2]]
# 输出："bacd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"
#
#
#  示例 2：
#
#  输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# 输出："abcd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[0] 和 s[2], s = "acbd"
# 交换 s[1] 和 s[2], s = "abcd"
#
#  示例 3：
#
#  输入：s = "cba", pairs = [[0,1],[1,2]]
# 输出："abc"
# 解释：
# 交换 s[0] 和 s[1], s = "bca"
# 交换 s[1] 和 s[2], s = "bac"
# 交换 s[0] 和 s[1], s = "abc"
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 10^5
#  0 <= pairs.length <= 10^5
#  0 <= pairs[i][0], pairs[i][1] < s.length
#  s 中只含有小写英文字母
#
#  Related Topics 并查集 数组
#  👍 229 👎 0


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            a = find(x)
            b = find(y)
            if a != b:
                f[b] = a

        for i, j in pairs:
            union(i, j)
        m = collections.defaultdict(list)
        for i, ch in enumerate(s):
            heapq.heappush(m[find(i)], ch)
        ans=['']*len(s)
        for i in range(len(ans)):
            ans[i]=heapq.heappop(m[find(i)])
        return ''.join(ans)


Solution().smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]])
