# 你将得到一个字符串数组 A。
#
#  每次移动都可以交换 S 的任意两个偶数下标的字符或任意两个奇数下标的字符。
#
#  如果经过任意次数的移动，S == T，那么两个字符串 S 和 T 是 特殊等价 的。
#
#  例如，S = "zzxy" 和 T = "xyzz" 是一对特殊等价字符串，因为可以先交换 S[0] 和 S[2]，然后交换 S[1] 和 S[3]，使得
#  "zzxy" -> "xzzy" -> "xyzz" 。
#
#  现在规定，A 的 一组特殊等价字符串 就是 A 的一个同时满足下述条件的非空子集：
#
#
#  该组中的每一对字符串都是 特殊等价 的
#  该组字符串已经涵盖了该类别中的所有特殊等价字符串，容量达到理论上的最大值（也就是说，如果一个字符串不在该组中，那么这个字符串就 不会 与该组内任何字符串特
# 殊等价）
#
#
#  返回 A 中特殊等价字符串组的数量。
#
#
#
#
#
#
#  示例 1：
#
#  输入：["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
# 输出：3
# 解释：
# 其中一组为 ["abcd", "cdab", "cbad"]，因为它们是成对的特殊等价字符串，且没有其他字符串与这些字符串特殊等价。
# 另外两组分别是 ["xyzz", "zzxy"] 和 ["zzyx"]。特别需要注意的是，"zzxy" 不与 "zzyx" 特殊等价。
#
#
#  示例 2：
#
#  输入：["abc","acb","bac","bca","cab","cba"]
# 输出：3
# 解释：3 组 ["abc","cba"]，["acb","bca"]，["bac","cab"]
#
#
#
#
#  提示：
#
#
#  1 <= A.length <= 1000
#  1 <= A[i].length <= 20
#  所有 A[i] 都具有相同的长度。
#  所有 A[i] 都只由小写字母组成。
#
#  Related Topics 字符串
#  👍 95 👎 0

from typing import List
import itertools
import collections


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        A = set(A)
        m2 = set()

        def cal(word):
            m = collections.defaultdict(list)
            for i, ch in enumerate(word):
                m[i % 2].append(ch)
            return collections.Counter(m[0]), collections.Counter(m[1])

        ans = 0
        for word in A:
            if word not in m2:
                m2.add(word)
                a, b = cal(word)
                for word2 in A:
                    if word2 in m2:
                        continue
                    c, d = cal(word2)
                    if a == c and b == d:
                        m2.add(word2)
                ans += 1
        return ans


# 技巧,计算所有字母在偶数位和奇数位出现的数量
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def count(word):
            ans = [0] * 52
            for i, ch in enumerate(word):
                ans[ord(ch)-ord('a')+ 26*(i%2)]+=1
            return tuple(ans)
        return len({count(word) for word in A})

Solution().numSpecialEquivGroups(["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"])
