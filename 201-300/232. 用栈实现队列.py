'''
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
 

示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
 

说明:

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 8
        self.q = [0] * self.len
        self.enum = 0
        self.head = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.enum < self.len:
            self.q[(self.head + self.enum) % self.len] = x
        else:
            oldlen = self.len
            self.len *= 2
            newq = [0] * self.len
            for i in range(oldlen):
                newq[i] = self.q[(i + self.head) % oldlen]
            self.q, self.head = newq, 0
            self.q[(self.enum + self.head) % self.len] = x
        self.enum += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        a = self.q[self.head]
        self.head = (self.head + 1) % self.len
        self.enum -= 1
        return a

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.q[self.head]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.enum == 0


a = MyQueue()
a.push(1)
a.push(2)
a.peek
