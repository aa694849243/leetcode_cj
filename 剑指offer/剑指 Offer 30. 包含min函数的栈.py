#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import heapq


# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
#
#
#
#  示例:
#
#  MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.
#
#
#
#
#  提示：
#
#
#  各函数的调用总次数不超过 20000 次
#
#
#
#
#  注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/
#  Related Topics 栈 设计
#  👍 151 👎 0

# 需要用辅助最小栈而不是堆
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.q = []
        self.m = collections.Counter()

    def push(self, x: int) -> None:
        self.stack.append(x)
        heapq.heappush(self.q, x)
        self.m[x] += 1

    def pop(self) -> None:
        a = self.stack.pop()
        self.m[a] -= 1

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        while self.m[self.q[0]] == 0:
            heapq.heappop(self.q)
        return self.q[0]

    # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
# leetcode submit region end(Prohibit modification and deletion)
