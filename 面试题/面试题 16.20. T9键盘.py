#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 在老式手机上，用户通过数字键盘输入，手机将提供与这些数字相匹配的单词列表。每个数字映射到0至4个字母。给定一个数字序列，实现一个算法来返回匹配单词的列表。你
# 会得到一张含有有效单词的列表。映射如下图所示：
#
#
#
#  示例 1:
#
#  输入: num = "8733", words = ["tree", "used"]
# 输出: ["tree", "used"]
#
#
#  示例 2:
#
#  输入: num = "2", words = ["a", "b", "c", "d"]
# 输出: ["a", "b", "c"]
#
#  提示：
#
#
#  num.length <= 1000
#  words.length <= 500
#  words[i].length == num.length
#  num中不会出现 0, 1 这两个数字
#
#  Related Topics 数组 哈希表 字符串
#  👍 26 👎 0


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        m = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        res = []
        n = len(num)

        # def dfs(i, s):
        #     if i == n:
        #         res.add(s)
        #         return
        #     for ch in m[int(num[i])]:
        #         dfs(i + 1, s + ch)
        def check(word):
            if len(word) != n:
                return False
            for i, val in enumerate(num):
                if word[i] not in m[int(val)]:
                    return False
            return True
        for word in words:
            if check(word):
                res.append(word)
        return res


Solution().getValidT9Words(num="8733", words=["tree", "used"])
