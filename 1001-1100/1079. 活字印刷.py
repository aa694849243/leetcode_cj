# -*- coding: utf-8 -*-
import itertools


# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
#
#  注意：本题中，每个活字字模只能使用一次。
#
#
#
#  示例 1：
#
#  输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
#
#
#  示例 2：
#
#  输入："AAABBC"
# 输出：188
#
#
#
#
#  提示：
#
#
#  1 <= tiles.length <= 7
#  tiles 由大写英文字母组成
#
#  Related Topics 回溯算法
#  👍 111 👎 0


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        m = set()
        for size in range(1, len(tiles) + 1):
            for a in itertools.permutations(tiles, size):
                m.add(''.join(a))
        return len(m)


# 回溯标准写法
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles=sorted(list(tiles))
        used = [False] * (n := len(tiles))
        self.num = 0

        def backtrack(used, sequence):
            if len(sequence) > 0:
                self.num += 1
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and not used[i - 1] and tiles[i] == tiles[i - 1]:  # i-1为False说明这个串中没用i-1这个字符，但之前的一定调用了i-1字符，用完后置为False了，若再用就重复了
                    continue
                used[i] = True
                backtrack(used, sequence + [tiles[i]])
                used[i] = False

        backtrack(used, [])
        return self.num


Solution().numTilePossibilities("AAB")
