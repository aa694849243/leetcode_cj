# 有一些工作：difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。
#
#  现在我们有一些工人。worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。
#
#  每一个工人都最多只能安排一个工作，但是一个工作可以完成多次。
#
#  举个例子，如果 3 个工人都尝试完成一份报酬为 1 的同样工作，那么总收益为 $3。如果一个工人不能完成任何工作，他的收益为 $0 。
#
#  我们能得到的最大收益是多少？
#
#
#
#  示例：
#
#  输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# 输出: 100
# 解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。
#
#
#
#  提示:
#
#
#  1 <= difficulty.length = profit.length <= 10000
#  1 <= worker.length <= 10000
#  difficulty[i], profit[i], worker[i] 的范围是 [1, 10^5]
#
#  Related Topics 双指针
#  👍 55 👎 0


from typing import List
import heapq


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        q = []
        for i in range(len(difficulty)):
            heapq.heappush(q, (-profit[i], difficulty[i]))
        worker.sort()

        def bis(l, r, target):
            while l < r:
                mid = (l + r) // 2
                if worker[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l

        ans = 0
        while worker and q:
            prof, dif = heapq.heappop(q)
            prof *= -1
            l, r = 0, len(worker),
            flag = bis(l, r, dif)
            ans += prof * (r - flag)
            worker = worker[:flag]
        return ans


Solution().maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25])
