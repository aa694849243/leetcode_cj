'''现在，我们用一些方块来堆砌一个金字塔。 每个方块用仅包含一个字母的字符串表示。

使用三元组表示金字塔的堆砌规则如下：

对于三元组 ABC ，C 为顶层方块，方块 A 、B 分别作为方块 C 下一层的的左、右子块。当且仅当 ABC 是被允许的三元组，我们才可以将其堆砌上。

初始时，给定金字塔的基层 bottom，用一个字符串表示。一个允许的三元组列表 allowed，每个三元组用一个长度为 3 的字符串表示。

如果可以由基层一直堆到塔尖就返回 true ，否则返回 false 。

 

示例 1：

输入：bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
输出：true
解释：
可以堆砌成这样的金字塔:
    A
   / \
  G   E
 / \ / \
B   C   D

因为符合 BCG、CDE 和 GEA 三种规则。
示例 2：

输入：bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
输出：false
解释：
无法一直堆到塔尖。
注意, 允许存在像 ABC 和 ABD 这样的三元组，其中 C != D。
 

提示：

bottom 的长度范围在 [2, 8]。
allowed 的长度范围在[0, 200]。
方块的标记字母范围为{'A', 'B', 'C', 'D', 'E', 'F', 'G'}

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pyramid-transition-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections


# 1深度优先搜索
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        m = collections.defaultdict(list)
        for word in allowed:
            m[word[:2]].append(word[2])

        def rec(bottom, i, li):
            if len(bottom) == 1:
                return True
            a = bottom[i - 1:i + 1]
            for ch in m[a]:
                li.append(ch)
                if i == len(bottom) - 1:
                    if rec(''.join(li), 1, []):
                        return True
                elif rec(bottom, i + 1, li):
                    return True
                li.pop()
            return False

        return rec(bottom, 1, [])


# 2状态转换
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        T = [[0] * (1 << 7) for _ in range(1 << 7)]
        for word in allowed:
            u, v, w = (1 << (ord(x) - ord('A')) for x in word)
            for i in range(1 << 7):
                if u & i:
                    for j in range(1 << 7):
                        if v & j:
                            T[i][j] |= w
        state = [1 << (ord(x) - ord('A')) for x in bottom]
        while len(state) > 1:
            for i in range(len(state) - 1):
                state[i] = T[state[i]][state[i + 1]]
            state.pop()
        return bool(state[0])


# class Solution(object):
#     def pyramidTransition(self, bottom, allowed):
#         T = [[0] * (1 << 7) for _ in range(1 << 7)]
#         for triple in allowed:
#             u, v, w = (1 << (ord(x) - ord('A')) for x in triple)
#             for b1 in range(1 << 7):
#                 if u & b1:
#                     for b2 in range(1 << 7):
#                         if v & b2:
#                             T[b1][b2] |= w
#
#         state = [1 << (ord(x) - ord('A')) for x in bottom]
#         while len(state) > 1:
#             for i in range(len(state) - 1):
#                 state[i] = T[state[i]][state[i+1]]
#             state.pop()
#         return bool(state[0])

Solution().pyramidTransition("CCC",
                             ["CBB", "ACB", "ABD", "CDB", "BDC", "CBC", "DBA", "DBB", "CAB", "BCB", "BCC", "BAA", "CCD", "BDD", "DDD", "CCA", "CAA",
                              "CCC", "CCB"])
