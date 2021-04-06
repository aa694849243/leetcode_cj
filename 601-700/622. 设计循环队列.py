'''设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
 

示例：

MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4
 

提示：

所有的值都在 0 至 1000 的范围内；
操作数将在 1 至 1000 的范围内；
请不要使用内置的队列库。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-circular-queue
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# 1数组
class MyCircularQueue:

    def __init__(self, k: int):
        self.ca = k
        self.cnt = 0
        self.m = [0] * k
        self.head = 0

    def enQueue(self, value: int) -> bool:
        if self.cnt >= self.ca:
            return False
        self.m[(self.head + self.cnt) % self.ca] = value
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.cnt == 0:
            return False
        self.head = (self.head + 1) % self.ca
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if self.cnt == 0:
            return -1
        return self.m[self.head]

    def Rear(self) -> int:
        if self.cnt == 0:
            return -1
        return self.m[(self.head + self.cnt - 1) % self.ca]

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.ca


# 2链表
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:

    def __init__(self, k: int):
        self.ca = k
        self.cnt = 0
        self.head = Node(0)
        self.rear = self.head
        self.rear.next = self.head

    def enQueue(self, value: int) -> bool:
        if self.cnt >= self.ca:
            return False
        if self.cnt == 0:
            self.head = Node(value)
            self.rear=self.head
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next
        self.rear.next = self.head
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.cnt == 0:
            return False
        self.head = self.head.next
        self.rear.next = self.head
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if self.cnt == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.cnt == 0:
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.ca


# ["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"]
# [[6],[6],[],[],[],[5],[],[],[],[],[],[]]
a = MyCircularQueue(6)
a.enQueue(6)
a.Rear()
a.Rear()
a.deQueue()
a.enQueue(5)
a.Rear()
a.deQueue()
a.Front()
