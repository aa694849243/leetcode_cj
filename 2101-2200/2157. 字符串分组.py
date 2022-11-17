# -*- coding: utf-8 -*-
# 给你一个下标从 0 开始的字符串数组 words 。每个字符串都只包含 小写英文字母 。words 中任意一个子串中，每个字母都至多只出现一次。
#
#  如果通过以下操作之一，我们可以从 s1 的字母集合得到 s2 的字母集合，那么我们称这两个字符串为 关联的 ：
#
#
#  往 s1 的字母集合中添加一个字母。
#  从 s1 的字母集合中删去一个字母。
#  将 s1 中的一个字母替换成另外任意一个字母（也可以替换为这个字母本身）。
#
#
#  数组 words 可以分为一个或者多个无交集的 组 。如果一个字符串与另一个字符串关联，那么它们应当属于同一个组。
#
#  注意，你需要确保分好组后，一个组内的任一字符串与其他组的字符串都不关联。可以证明在这个条件下，分组方案是唯一的。
#
#  请你返回一个长度为 2 的数组 ans ：
#
#
#  ans[0] 是 words 分组后的 总组数 。
#  ans[1] 是字符串数目最多的组所包含的字符串数目。
#
#
#
#
#  示例 1：
#
#
# 输入：words = ["a","b","ab","cde"]
# 输出：[2,3]
# 解释：
# - words[0] 可以得到 words[1] （将 'a' 替换为 'b'）和 words[2] （添加 'b'）。所以 words[0] 与
# words[1] 和 words[2] 关联。
# - words[1] 可以得到 words[0] （将 'b' 替换为 'a'）和 words[2] （添加 'a'）。所以 words[1] 与
# words[0] 和 words[2] 关联。
# - words[2] 可以得到 words[0] （删去 'b'）和 words[1] （删去 'a'）。所以 words[2] 与 words[0] 和
# words[1] 关联。
# - words[3] 与 words 中其他字符串都不关联。
# 所以，words 可以分成 2 个组 ["a","b","ab"] 和 ["cde"] 。最大的组大小为 3 。
#
#
#  示例 2：
#
#
# 输入：words = ["a","ab","abc"]
# 输出：[1,3]
# 解释：
# - words[0] 与 words[1] 关联。
# - words[1] 与 words[0] 和 words[2] 关联。
# - words[2] 与 words[1] 关联。
# 由于所有字符串与其他字符串都关联，所以它们全部在同一个组内。
# 所以最大的组大小为 3 。
#
#
#
#
#  提示：
#
#
#  1 <= words.length <= 2 * 10⁴
#  1 <= words[i].length <= 26
#  words[i] 只包含小写英文字母。
#  words[i] 中每个字母最多只出现一次。
#
#
#  Related Topics 位运算 并查集 字符串
#  👍 40 👎 0
import collections
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:

        def trans(word):
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - 97))
            return mask

        c = collections.Counter()
        for word in words:
            c[trans(word)] += 1
        visted = set()

        def gather(mask):
            size = c[mask]
            T = [mask]
            visted.add(mask)
            while 1:
                tree = []
                for msk in T:
                    for i in range(26):
                        tmp_add_1 = msk | (1 << i) #考察+1格
                        if tmp_add_1 not in visted and tmp_add_1 in c:
                            tree.append(tmp_add_1)
                            visted.add(tmp_add_1)
                            size += c[tmp_add_1]
                        if tmp_add_1 != msk: #考察replace
                            for j in range(26):
                                if tmp_add_1&(1<<j):
                                    tmp_replace = tmp_add_1^(1<<j)
                                    if tmp_replace not in visted and tmp_replace in c:
                                        tree.append(tmp_replace)
                                        visted.add(tmp_replace)
                                        size += c[tmp_replace]
                    for k in range(26): #考察-1格
                        if msk&(1<<k):
                            tmp_sub_1 = msk^(1<<k)
                            if tmp_sub_1 not in visted and tmp_sub_1 in c:
                                tree.append(tmp_sub_1)
                                visted.add(tmp_sub_1)
                                size += c[tmp_sub_1]
                if not tree:
                    break
                T = tree
            return size
        gropus = 0
        max_size = 0
        for mask in c:
            if mask not in visted:
                max_size=max(max_size,gather(mask))
                gropus+=1
        return [gropus,max_size]
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().groupStrings( ["vd","dv"]))