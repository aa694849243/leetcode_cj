#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：pu
# sh、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。
#
#  示例1:
#
#   输入：
# ["SortedStack", "push", "push", "peek", "pop", "peek"]
# [[], [1], [2], [], [], []]
#  输出：
# [null,null,null,1,null,2]
#
#
#  示例2:
#
#   输入：
# ["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
# [[], [], [], [1], [], []]
#  输出：
# [null,null,null,null,null,true]
#
#
#  说明:
#
#
#  栈中的元素数目在[0, 5000]范围内。
#
#  Related Topics 栈 设计 单调栈
#  👍 39 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class SortedStack:

    def __init__(self):
        self.less = []
        self.greater = []

    def push(self, val: int) -> None:
        while self.less and val > self.less[-1]:
            self.greater.append(self.less.pop())
        while self.greater and self.greater[-1]>val:
            self.less.append(self.greater.pop())
        self.less.append(val)

    def pop(self) -> None:
        while self.greater:
            self.less.append(self.greater.pop())
        if not self.less:
            return
        self.less.pop()

    def peek(self) -> int:
        while self.greater:
            self.less.append(self.greater.pop())
        if not self.less:
            return -1
        return self.less[-1]

    def isEmpty(self) -> bool:
        return not self.less and not self.greater
["SortedStack", "push", "push", "push", "pop", "push", "push", "isEmpty", "pop", "pop", "push", "peek", "isEmpty", "pop", "peek", "push", "push", "peek", "isEmpty", "isEmpty", "isEmpty", "isEmpty", "isEmpty", "push", "push", "push", "push", "push", "peek", "peek", "isEmpty", "push"]
[[], [52], [63],  [47], [], [45], [52], [], [], [], [17], [], [], [], [], [6], [30], [], [], [], [], [], [], [51], [46], [2], [56], [39], [], [], [], [38]]

# Your SortedStack object will be instantiated and called as such:
obj = SortedStack()
obj.push(45)
obj.push(52)
obj.push(17)
obj.peek()
obj.pop()
obj.peek
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
# leetcode submit region end(Prohibit modification and deletion)
