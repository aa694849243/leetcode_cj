# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 设计一个电话目录管理系统，让它支持以下功能：
#
#
#  get: 分配给用户一个未被使用的电话号码，获取失败请返回 -1
#  check: 检查指定的电话号码是否被使用
#  release: 释放掉一个电话号码，使其能够重新被分配
#
#
#
#
#  示例：
#
#  // 初始化电话目录，包括 3 个电话号码：0，1 和 2。
# PhoneDirectory directory = new PhoneDirectory(3);
#
# // 可以返回任意未分配的号码，这里我们假设它返回 0。
# directory.get();
#
# // 假设，函数返回 1。
# directory.get();
#
# // 号码 2 未分配，所以返回为 true。
# directory.check(2);
#
# // 返回 2，分配后，只剩一个号码未被分配。
# directory.get();
#
# // 此时，号码 2 已经被分配，所以返回 false。
# directory.check(2);
#
# // 释放号码 2，将该号码变回未分配状态。
# directory.release(2);
#
# // 号码 2 现在是未分配状态，所以返回 true。
# directory.check(2);
#
#
#
#
#  提示：
#
#
#  1 <= maxNumbers <= 10^4
#  0 <= number < maxNumbers
#  调用方法的总数处于区间 [0 - 20000] 之内
#
#  Related Topics 设计 队列 数组 哈希表 链表 👍 30 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.n = maxNumbers
        self.m = {}

    def get(self) -> int:
        for i in range(self.n):
            if i not in self.m:
                self.m[i] = 1
                return i
        return -1

    def check(self, number: int) -> bool:
        return number not in self.m

    def release(self, number: int) -> None:
        if number in self.m:
            self.m.pop(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
# leetcode submit region end(Prohibit modification and deletion)
