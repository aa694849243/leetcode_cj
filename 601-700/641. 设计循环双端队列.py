'''设计实现双端队列。
你的实现需要支持以下操作：

MyCircularDeque(k)：构造函数,双端队列的大小为k。
insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
isEmpty()：检查双端队列是否为空。
isFull()：检查双端队列是否满了。
示例：

MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			        // 返回 true
circularDeque.insertLast(2);			        // 返回 true
circularDeque.insertFront(3);			        // 返回 true
circularDeque.insertFront(4);			        // 已经满了，返回 false
circularDeque.getRear();  				// 返回 2
circularDeque.isFull();				        // 返回 true
circularDeque.deleteLast();			        // 返回 true
circularDeque.insertFront(4);			        // 返回 true
circularDeque.getFront();				// 返回 4
 
 

提示：

所有值的范围为 [1, 1000]
操作次数的范围为 [1, 1000]
请不要使用内置的双端队列库。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-circular-deque
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_0 = obj.insertFront(value)
# param_1 = obj.insertLast(value)
# param_2 = obj.deleteFront()
# param_3 = obj.deleteLast()
# param_4 = obj.getFront()
# param_5 = obj.getRear()
# param_6 = obj.isEmpty()
# param_7 = obj.isFull()
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.count = 0
        self.head = Node(0)
        self.rare = Node(0)
        self.head.next = self.rare
        self.rare.prev = self.head

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.count >= self.k:
            return False
        p = self.head.next
        self.head.next = Node(value)
        self.head.next.next = p
        self.head.next.prev = self.head
        p.prev = self.head.next
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.count >= self.k:
            return False
        p = self.rare.prev
        self.rare.prev = Node(value)
        self.rare.prev.prev = p
        self.rare.prev.next = p
        p.next = self.rare.prev
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.count == 0: return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.count == 0: return False
        self.rare.prev = self.rare.prev.prev
        self.rare.prev.next = self.rare
        self.count -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.count==0:return -1
        return self.head.next.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.count==0: return -1
        return self.rare.prev.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.count==0 else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return True if self.count==self.k else False
["MyCircularDeque","insertFront","getRear","deleteLast","getRear","insertFront","insertFront","insertFront","insertFront","isFull"]
[[77],[89],[],[],[],[19],[23],[23],[82],[],[45],[],[],[],[],[],[74],[],[],[98],[],[99],[],[],[],[],[],[],[8],[],[],[],[],[],[75],[],[],[35],[59],[],[],[],[],[22],[],[],[],[],[],[],[],[],[],[],[],[21],[],[26],[63],[],[],[],[],[87],[76],[],[],[],[26],[],[67],[],[],[],[],[36],[],[],[],[72],[],[87],[],[],[],[],[85],[],[],[91],[],[],[],[],[],[],[],[],[],[34],[44],[]]