#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(
# 1)。 示例： MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0);
#  minStack.push(-3); minStack.getMin();   --> 返回 -3. minStack.pop(); minStack.top
# ();      --> 返回 0. minStack.getMin();   --> 返回 -2. Related Topics 栈 设计
#  👍 53 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.m = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.m:
            self.m.append(x)
        else:
            self.m.append(min(self.m[-1], x))

    def pop(self) -> None:
        if not self.stack:
            return
        self.m.pop()
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return -1
        return self.m[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
