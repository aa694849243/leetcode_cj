import collections, heapq, itertools
from typing import List


# 给定一个字符串数组 words，找到以 words 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中 任意一个 即可。
#
#
#  我们可以假设 words 中没有字符串是 words 中另一个字符串的子字符串。
#
#
#
#  示例 1：
#
#
# 输入：words = ["alex","loves","leetcode"]
# 输出："alexlovesleetcode"
# 解释："alex"，"loves"，"leetcode" 的所有排列都会被接受。
#
#  示例 2：
#
#
# 输入：words = ["catg","ctaagt","gcta","ttca","atgcatc"]
# 输出："gctaagttcatgcatc"
#
#
#
#  提示：
#
#
#  1 <= words.length <= 12
#  1 <= words[i].length <= 20
#  words[i] 由小写英文字母组成
#  words 中的所有字符串 互不相同
#
#  Related Topics 动态规划
#  👍 77 👎 0

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        overlap_m = {}

        def overlap(i, j):  # 计算两个word的覆盖程度
            s1, s2 = words[i], words[j]
            ans = 0
            for k in range(1, len(s1)):
                if s1[k:] == s2[:len(s1[k:])]:
                    ans = len(s1[k:])
                    break
            overlap_m[i, j] = ans
            return ans

        n = len(words)
        m = {}
        parent = [[None] * n for _ in range(1 << n)]  # 计算每个状态的上一个节点，方便还原

        def dp(status, last):  # 动态规划，dp(1111,x) 计算不同x为最后一个字母的覆盖程度最大值
            if (status, last) in m:
                return m[status, last]
            ans = -1
            pre = status ^ (1 << last)
            for i in range(n):
                if pre & (1 << i):
                    a = dp(pre, i)
                    b = overlap_m[i, last]
                    if a + b > ans:
                        ans = a + b
                        parent[status][last] = i
            m[status, last] = ans
            return ans

        for i in range(n):
            for j in range(n):
                if i != j:
                    overlap_m[i, j] = overlap(i, j)
                    overlap_m[j, i] = overlap(j, i)
        for i in range(n):  # 初始化
            m[1 << i, i] = 0
            parent[1 << i][i] = -1  # 只有一个节点，的前继节点为-1,作为终止情况
        for i in range(n):
            dp((1 << n) - 1, i)
        ans = -1
        for i in range(n):
            if m[(1 << n) - 1, i] > ans:
                first = i
                ans = m[(1 << n) - 1, i]
        perm = [first]
        status = (1 << n) - 1
        while parent[status][first] > -1:
            nxt = parent[status][first]
            perm.append(nxt)
            status ^= (1 << first)
            first = nxt
        perm = perm[::-1]
        ans = ''
        for i in range(1, n):
            cnt = overlap_m[perm[i - 1], perm[i]]
            word = words[perm[i - 1]]
            ans += word[:len(word) - cnt]
        ans += words[perm[-1]]
        return ans


Solution().shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"])
