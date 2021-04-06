'''
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

# caojie 5%
class CQueue:

    def __init__(self):
        self.len_ = 0
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)
        self.len_ += 1

    def deleteHead(self) -> int:
        if self.len_ == 0:
            return -1
        else:
            while len(self.stack1) > 1:
                self.stack2.append(self.stack1.pop())
            x = self.stack1.pop()
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            self.len_ -= 1
            return x


# 改良版下·
# 整个队列分成两个列表拼合而成

class CQueue:

    def __init__(self):
        self.len_ = 0
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)  # stack1维护入队

    def deleteHead(self) -> int:
        if self.stack2: return self.stack2.pop()  # stack2维护出队
        if not self.stack1: return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
