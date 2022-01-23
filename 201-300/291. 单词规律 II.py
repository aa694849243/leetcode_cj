#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给你一种规律 pattern 和一个字符串 str，请你判断 str 是否遵循其相同的规律。
#
#  这里我们指的是 完全遵循，例如 pattern 里的每个字母和字符串 str 中每个 非空 单词之间，存在着 双射 的对应规律。双射 意味着映射双方一一对
# 应，不会存在两个字符映射到同一个字符串，也不会存在一个字符分别映射到两个不同的字符串。
#
#
#
#  示例 1：
#
#
# 输入：pattern = "abab", s = "redblueredblue"
# 输出：true
# 解释：一种可能的映射如下：
# 'a' -> "red"
# 'b' -> "blue"
#
#  示例 2：
#
#
# 输入：pattern = "aaaa", s = "asdasdasdasd"
# 输出：true
# 解释：一种可能的映射如下：
# 'a' -> "asd"
#
#
#  示例 3：
#
#
# 输入：pattern = "abab", s = "asdasdasdasd"
# 输出：true
# 解释：一种可能的映射如下：
# 'a' -> "a"
# 'b' -> "sdasd"
# 注意 'a' 和 'b' 不能同时映射到 "asd"，因为这里的映射是一种双射。
#
#
#  示例 4：
#
#
# 输入：pattern = "aabb", s = "xyzabcxzyabc"
# 输出：false
#
#
#
#
#  提示：
#
#
#  0 <= pattern.length <= 20
#  0 <= s.length <= 50
#  pattern 和 s 由小写英文字母组成
#
#  Related Topics 哈希表 字符串 回溯
#  👍 65 👎 0


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def dfs(pa, s_, d, d2):
            if len(pa) > len(s_):
                return False
            if len(pa) == 1:
                if pa[0] not in d and s_ not in d2:
                    return True
                elif pa[0] in d and s_ in d2 and d[pa[0]]==s_ and d2[s_]==pa[0]:
                    return True
                else:
                    return False
            for i in range(1, len(s_)):
                a, b = s_[:i], s_[i:]
                if pa[0] not in d and a not in d2:
                    d[pa[0]] = a
                    d2[a] = pa[0]
                    if dfs(pa[1:], b, d, d2):
                        return True
                    d.pop(pa[0])
                    d2.pop(a)
                elif pa[0] in d and a in d2 and d[pa[0]] == a and d2[a] == pa[0]:
                    if dfs(pa[1:], b, d, d2):
                        return True
            return False

        return dfs(pattern, s, {},{})


print(Solution().wordPatternMatch("ab", "aa"))
