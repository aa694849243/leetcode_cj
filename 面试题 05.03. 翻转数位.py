#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。
#
#  示例 1：
#
#  输入: num = 1775(110111011112)
# 输出: 8
#
#
#  示例 2：
#
#  输入: num = 7(01112)
# 输出: 4
#
#  Related Topics 位运算 动态规划
#  👍 44 👎 0

# 动态规划 滑窗请看c++
class Solution:
    def reverseBits(self, num: int) -> int:
        ans, cur, pre = 0, 0, 0
        for i in range(32):
            if num & (1 << i):
                cur += 1
                pre += 1
            else:
                pre = cur + 1
                cur = 0
            ans = max(ans, pre)
        return ans


Solution().reverseBits(236387)
