'''中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-median-from-data-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 用二分法速度会更快
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.count = 0

    def addNum(self, num: int) -> None:
        flag = 1
        if not self.l:
            self.l.append(num)
        else:
            for i in range(len(self.l)):
                if self.l[i] > num:
                    flag = 0
                    self.l.insert(i, num)
                    break
            if flag:
                self.l.insert(i + 1, num)
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (self.l[self.count // 2] + self.l[self.count // 2 - 1]) / 2
        else:
            return self.l[self.count // 2]
# 堆排序
import heapq_max
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count=0
        self.left=[]
        self.right=[]

    def addNum(self, num: int) -> None:
        heapq_max.heappush_max(self.left,num)
        a=heapq_max.heappop_max(self.left)
        heapq.heappush(self.right,a)
        if not self.count%2:
            b=heapq.heappop(self.right)
            heapq_max.heappush_max(self.left,b)
        self.count+=1

    def findMedian(self) -> float:
        if self.count%2:
            return self.left[0]
        return (self.left[0]+self.right[0])/2

#大顶堆
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count=0
        self.left=[]
        self.right=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.right,-heapq.heappushpop(self.left,-num))
        if not self.count%2:
            heapq.heappush(self.left,-heapq.heappop(self.right))
        self.count+=1

    def findMedian(self) -> float:
        if self.count%2:
            return -self.left[0]
        return (-self.left[0]+self.right[0])/2
x=MedianFinder()
x.addNum(3)
x.addNum(2)
x.addNum(4)
x.findMedian()