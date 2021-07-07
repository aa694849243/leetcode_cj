# -*- coding: utf-8 -*-
import collections
from typing import List


# 给你一个方程，左边用 words 表示，右边用 result 表示。
#
#  你需要根据以下规则检查方程是否可解：
#
#
#  每个字符都会被解码成一位数字（0 - 9）。
#  每对不同的字符必须映射到不同的数字。
#  每个 words[i] 和 result 都会被解码成一个没有前导零的数字。
#  左侧数字之和（words）等于右侧数字（result）。
#
#
#  如果方程可解，返回 True，否则返回 False。
#
#
#
#  示例 1：
#
#  输入：words = ["SEND","MORE"], result = "MONEY"
# 输出：true
# 解释：映射 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
# 所以 "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
#
#  示例 2：
#
#  输入：words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
# 输出：true
# 解释：映射 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->
# 4
# 所以 "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
#
#  示例 3：
#
#  输入：words = ["THIS","IS","TOO"], result = "FUNNY"
# 输出：true
#
#
#  示例 4：
#
#  输入：words = ["LEET","CODE"], result = "POINT"
# 输出：false
#
#
#
#
#  提示：
#
#
#  2 <= words.length <= 5
#  1 <= words[i].length, results.length <= 7
#  words[i], result 只含有大写英文字母
#  表达式中使用的不同字符数最大为 10
#
#  Related Topics 数组 数学 字符串 回溯算法
#  👍 49 👎 0

# 1dfs+剪枝
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        rep = collections.defaultdict(lambda: -1)
        lead_zero = collections.defaultdict(int)
        used = [False] * 10
        for word in words:
            if len(word) > len(result):
                return False
            if len(word) > 1:
                lead_zero[word[0]] = 1
        n = len(result)
        nw = len(words)
        lead_zero[result[0]] = 1 if n > 1 else 0
        carry = [0] * (n + 2)  # 最高位数

        def dfs(pos, iden):
            if abs(pos) == n + 1:
                return carry[pos] == 0
            if iden < nw:
                w = words[iden]
                if abs(pos) > len(w) or rep[w[pos]] != -1:
                    return dfs(pos, iden + 1)
                for i in range(lead_zero[w[pos]], 10):
                    if not used[i]:
                        used[i] = True
                        rep[w[pos]] = i
                        check = dfs(pos, iden + 1)
                        if check:
                            return True
                        used[i] = False
                        rep[w[pos]] = -1
                return False
            else:
                left = sum(rep[word[pos]] for word in words if len(word) >= abs(pos)) + carry[pos]
                carry[pos - 1], left = divmod(left, 10)  # 这里不需要重置carry,因为每一轮计算result等式时，carry[pos-1]都重置了
                ch = result[pos]
                if rep[ch] == left:
                    return dfs(pos - 1, 0)
                elif rep[ch] == -1 and not used[left] and not (lead_zero[ch] == 1 and left == 0):
                    used[left], rep[ch] = True, left
                    check = dfs(pos - 1, 0)
                    used[left], rep[ch] = False, -1
                    return check
                else:
                    return False

        return dfs(-1, 0)


# dfs+模糊剪枝
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        rep = collections.defaultdict(int)
        lead_zero = collections.defaultdict(int)
        used = [False] * 10
        for word in words:
            if len(word) > 1:
                lead_zero[word[0]] = 1
            if len(word)>len(result):
                return False
            for i, ch in enumerate(word[::-1]):
                rep[ch] += 10 ** i
        lead_zero[result[0]] = 1 if len(result) > 1 else 0
        for i, ch in enumerate(result[::-1]):
            rep[ch] -= 10 ** i
        li = sorted(list(rep.items()), key=lambda x: -abs(x[1]))  # 绝对值逆序，先放大的后放小的
        suffix_max = [0] * len(li)
        suffix_min = [0] * len(li)
        for i in range(len(li)):  # li[i:]是因为前面已经确定了的值就不用再考虑了
            suffix_pos = [x[1] for x in li[i:] if x[1] > 0]  # 绝对值从大到小排序
            suffix_neg = [x[1] for x in li[i:] if x[1] < 0]  # 绝对值从大到小排序
            # sufix_min为负的最大+正的最小
            suffix_min[i] = sum(x * j for x, j in zip(suffix_neg, list(range(9, 9 - len(suffix_neg), -1))))
            suffix_min[i] += sum(x * j for x, j in zip(suffix_pos, list(range(len(suffix_pos)))))
            # suffix_max为正的最大+负的最小
            suffix_max[i] = sum(x * j for x, j in zip(suffix_pos, list(range(9, 9 - len(suffix_pos), -1))))
            suffix_max[i] += sum(x * j for x, j in zip(suffix_neg, list(range(len(suffix_pos)))))
        n = len(li)

        def dfs(pos, total):
            if pos == n:
                return total == 0
            if total < -abs(suffix_max[pos]) or total > abs(suffix_min[pos]):
                return False
            if li[pos][1] == 0:
                return dfs(pos + 1, total)
            ch,coeff = li[pos]
            for i in range(lead_zero[ch], 10):
                if not used[i]:
                    used[i]=True
                    check=dfs(pos+1,total+coeff*i)
                    if check:
                        return True
                    used[i]=False
            return False
        return dfs(0,0)


Solution().isSolvable(["HOPE","THIS","HELPS","OTHER"], "PEOPLE")
