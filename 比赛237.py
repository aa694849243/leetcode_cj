# 5734. 判断句子是否为全字母句
import collections


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = collections.Counter(sentence)
        return True if len(a) == 26 else False


# 5735. 雪糕的最大数量
from typing import List
import heapq


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cnt = 0
        heapq.heapify(costs)
        while costs and coins >= costs[0]:
            coins -= heapq.heappop(costs)
            cnt += 1
        return cnt


# 5736. 单线程 CPU
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        q = []
        tasks = [(time, process, i) for i, (time, process) in enumerate(tasks)]
        heapq.heapify(tasks)
        ans = []
        a = heapq.heappop(tasks)
        flag = a[0]
        heapq.heappush(q, (a[1], a[2], a[0]))
        while tasks or q:
            while tasks and tasks[0][0] <= flag:
                time, process, i = heapq.heappop(tasks)
                heapq.heappush(q, (process, i, time))
            if tasks and not q:
                time, process, i = heapq.heappop(tasks)
                heapq.heappush(q, (process, i, time))
                flag = q[0][2]
            process, i, time = heapq.heappop(q)
            ans.append(i)
            flag = flag + process
        return ans

Solution().getOrder([[5, 6], [9, 4], [3, 9], [3, 7], [1, 1], [6, 9], [9, 1]])
# 5737. 所有数对按位与结果的异或和
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        a = 0
        for i, num in arr1:
            a ^= num
        b = 0
        for j, num in arr2:
            b ^= num
        return a & b


Solution().getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]])
