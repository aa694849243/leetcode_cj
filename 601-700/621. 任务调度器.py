'''给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。

然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的 最短时间 。

 

示例 1：

输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。
示例 2：

输入：tasks = ["A","A","A","B","B","B"], n = 0
输出：6
解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
诸如此类
示例 3：

输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
输出：16
解释：一种可能的解决方案是：
     A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A
 

提示：

1 <= task.length <= 104
tasks[i] 是大写英文字母
n 的取值范围为 [0, 100]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/task-scheduler
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
# 1模拟
import heapq
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = collections.Counter(tasks)
        a = []
        for task in m:
            heapq.heappush(a, (-m[task], 1, task))
        time = 0
        res = []
        while a:
            time += 1
            for i in range(len(a)):
                if a[i][1] <= time:
                    x = a.pop(i)
                    x = (-(-x[0] - 1), x[1] + n + 1, x[2])
                    if x[0] != 0:
                        heapq.heappush(a, x)
                    res.append(x[2])
                    break
            else:
                res.append('待命')
        return time


# 2构造
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = collections.Counter(tasks)
        ma = max(m.values())
        cnt = 0
        for task in m:
            if m[task] == ma:
                cnt += 1
        return max(len(tasks), (ma - 1) * (n + 1) + cnt)


Solution().leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2)
