# 这个问题是 LeetCode 平台新增的交互式问题 。
#
#  我们给出了一个由一些独特的单词组成的单词列表，每个单词都是 6 个字母长，并且这个列表中的一个单词将被选作秘密。
#
#  你可以调用 master.guess(word) 来猜单词。你所猜的单词应当是存在于原列表并且由 6 个小写字母组成的类型字符串。
#
#  此函数将会返回一个整型数字，表示你的猜测与秘密单词的准确匹配（值和位置同时匹配）的数目。此外，如果你的猜测不在给定的单词列表中，它将返回 -1。
#
#  对于每个测试用例，你有 10 次机会来猜出这个单词。当所有调用都结束时，如果您对 master.guess 的调用不超过 10 次，并且至少有一次猜到秘密
# ，那么您将通过该测试用例。
#
#  除了下面示例给出的测试用例外，还会有 5 个额外的测试用例，每个单词列表中将会有 100 个单词。这些测试用例中的每个单词的字母都是从 'a' 到 'z'
#  中随机选取的，并且保证给定单词列表中的每个单词都是唯一的。
#
#  示例 1:
# 输入: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
#
# 解释:
#
# master.guess("aaaaaa") 返回 -1, 因为 "aaaaaa" 不在 wordlist 中.
# master.guess("acckzz") 返回 6, 因为 "acckzz" 就是秘密，6个字母完全匹配。
# master.guess("ccbazz") 返回 3, 因为 "ccbazz" 有 3 个匹配项。
# master.guess("eiowzz") 返回 2, 因为 "eiowzz" 有 2 个匹配项。
# master.guess("abcczz") 返回 4, 因为 "abcczz" 有 4 个匹配项。
#
# 我们调用了 5 次master.guess，其中一次猜到了秘密，所以我们通过了这个测试用例。
#
#
#  提示：任何试图绕过评判的解决方案都将导致比赛资格被取消。
#  Related Topics 极小化极大
#  👍 76 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def guess(self, word: str) -> int:
        a="acckzz"
        return sum(i==j for i,j in zip(a,word))


# 1极小极大化
# 1个字符串与正确字符串匹配度为3，那么接着找列表里匹配度为3的字符串
# 极小极大化：每个单词有7个匹配度，每个匹配度对应一个group，最坏情况下我们选择的下一个单词需要找maxgroup单词，所以我们选择的单词应该选择maxgroup最小的那个
from typing import List
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        n = len(wordlist)
        H = [[sum(a == b for a, b in zip(wordlist[i], wordlist[j])) for j in range(n)] for i in range(n)]
        possible = list(range(n))
        m = [0] * n

        def solve(possible):
            ansgrp, ansguss = possible, None
            for i in possible:
                if not m[i]:
                    groups = [[] for _ in range(7)]
                    for j in possible:
                        if j != i and not m[j]:
                            groups[H[i][j]].append(j)
                    maxgroup = max(groups, key=len)
                    if len(maxgroup) < len(ansgrp):
                        ansgrp, ansguss = maxgroup, i
            return ansguss

        while possible:
            guess = solve(possible)
            matches = master.guess(wordlist[guess])
            if matches == 6: return
            m[guess] = 1
            possible=[j for j in possible if not m[j] and H[guess][j]==matches]
Solution().findSecretWord(["acckzz","ccbazz","eiowzz","abcczz"],Master)

