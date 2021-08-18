#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 假设你正在读取一串整数。每隔一段时间，你希望能找出数字 x 的秩(小于或等于 x 的值的个数)。请实现数据结构和算法来支持这些操作，也就是说：
#
#  实现 track(int x) 方法，每读入一个数字都会调用该方法；
#
#  实现 getRankOfNumber(int x) 方法，返回小于或等于 x 的值的个数。
#
#  注意：本题相对原题稍作改动
#
#  示例:
#
#  输入:
# ["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
# [[], [1], [0], [0]]
# 输出:
# [null,0,null,1]
#
#
#  提示：
#
#
#  x <= 50000
#  track 和 getRankOfNumber 方法的调用次数均不超过 2000 次
#
#  Related Topics 设计 树状数组 二分查找 数据流
#  👍 20 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class StreamRank:

    def __init__(self):
        self.li = [0] * 50002

    @staticmethod
    def lowbit(num):
        return num & -num

    def track(self, x: int) -> None:
        x+=1
        while x <= 50001:
            self.li[x] += 1
            x += self.lowbit(x)

    def getRankOfNumber(self, x: int) -> int:
        ans = 0
        x+=1
        while x > 0:
            ans += self.li[x]
            x -= self.lowbit(x)
        return ans
obj = StreamRank()
obj.track(0)
obj.getRankOfNumber(0)
