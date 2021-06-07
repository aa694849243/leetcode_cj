# -*- coding: utf-8 -*-
# 给你一个字符串 s ，请你判断它是否 有效 。
#  字符串 s 有效 需要满足：假设开始有一个空字符串 t = "" ，你可以执行 任意次 下述操作将 t 转换为 s ：
#
#
#  将字符串 "abc" 插入到 t 中的任意位置。形式上，t 变为 tleft + "abc" + tright，其中 t == tleft + trigh
# t 。注意，tleft 和 tright 可能为 空 。
#
#
#  如果字符串 s 有效，则返回 true；否则，返回 false。
#
#
#
#  示例 1：
#
#
# 输入：s = "aabcbc"
# 输出：true
# 解释：
# "" -> "abc" -> "aabcbc"
# 因此，"aabcbc" 有效。
#
#  示例 2：
#
#
# 输入：s = "abcabcababcc"
# 输出：true
# 解释：
# "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
# 因此，"abcabcababcc" 有效。
#
#  示例 3：
#
#
# 输入：s = "abccba"
# 输出：false
# 解释：执行操作无法得到 "abccba" 。
#
#  示例 4：
#
#
# 输入：s = "cababc"
# 输出：false
# 解释：执行操作无法得到 "cababc" 。
#
#
#
#  提示：
#
#
#  1 <= s.length <= 2 * 104
#  s 由字母 'a'、'b' 和 'c' 组成
#
#  Related Topics 栈 字符串
#  👍 48 👎 0


class Solution:
    def isValid(self, s: str) -> bool:
        def dfs(s):
            if 'abc' not in s:
                return False
            if s == 'abc':
                return True
            i=s.index('abc')
            return dfs(s[:i]+s[i+3:])
        return dfs(s)
Solution().isValid("aabcbc")