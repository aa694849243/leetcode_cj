'''
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
 

示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
 

提示：

pop、top 和 getMin 操作总是在 非空栈 上调用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1=[]
        self.stack2=[]
        self.stack3=[]


    def push(self, x: int) -> None:
        while self.stack1 and self.stack1[-1]>x:
            self.stack2.append(self.stack1.pop())
        while self.stack2 and self.stack2[-1]<x:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)
        self.stack3.append(x)


    def pop(self) -> None:
        a=self.stack3.pop()
        if a in self.stack1:
            self.stack1.remove(a)
        else:
            self.stack2.remove(a)


    def top(self) -> int:
        return self.stack3[-1]


    def getMin(self) -> int:
        return self.stack1[0] if self.stack1 else self.stack2[-1]



# 官方 辅助栈
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


minStack = MinStack()
minStack.push(-10)
minStack.push(14)
minStack.getMin()
minStack.getMin()
minStack.push(-20)
minStack.getMin()
minStack.getMin()
minStack.top()
minStack.getMin()
minStack.pop()
minStack.push(10)
minStack.push(-7)
minStack.getMin()


minStack.getMin()
minStack.getMin()

