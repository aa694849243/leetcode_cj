# 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。
#
#
#  例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "t
# ars"，"rats"，或 "arts" 相似。
#
#  总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同
# 一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
#
#  给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？
#
#
#
#  示例 1：
#
#
# 输入：strs = ["tars","rats","arts","star"]
# 输出：2
#
#
#  示例 2：
#
#
# 输入：strs = ["omv","ovm"]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= strs.length <= 300
#  1 <= strs[i].length <= 300
#  strs[i] 只包含小写字母。
#  strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。
#
#
#
#
#  备注：
#
#  字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。
#  Related Topics 深度优先搜索 并查集 图
#  👍 122 👎 0


from typing import List


# 相似字符串
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        f = {}
        n = len(strs)

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def check(s1, s2):
            dif = 0
            for i in range(len(s1)):
                if s1[i] == s2[i]:
                    continue
                dif += 1
                if dif > 2:
                    return False
            return True

        def union(x, y):
            f[find(y)] = find(x)

        for i in range(n):
            for j in range(i + 1, n):
                s1, s2 = strs[i], strs[j]
                if find(i) == find(j):
                    continue
                elif check(s1, s2):
                    union(j, i)
        return sum(1 for i in range(n) if f[i] == i)
