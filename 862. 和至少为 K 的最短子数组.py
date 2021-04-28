# 返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
#
#  如果没有和至少为 K 的非空子数组，返回 -1 。
#
#
#
#
#
#
#  示例 1：
#
#  输入：A = [1], K = 1
# 输出：1
#
#
#  示例 2：
#
#  输入：A = [1,2], K = 4
# 输出：-1
#
#
#  示例 3：
#
#  输入：A = [2,-1,2], K = 3
# 输出：3
#
#
#
#
#  提示：
#
#
#  1 <= A.length <= 50000
#  -10 ^ 5 <= A[i] <= 10 ^ 5
#  1 <= K <= 10 ^ 9
#
#  Related Topics 队列 二分查找
#  👍 277 👎 0

from typing import List
import itertools
import collections


# 1单调队列
# 维护一个队列，队列存储累加和的下标，累加和需要递增，因为每次入队一个数作为终点，如果下滑那么这个数是不用考虑的，因为前面那个数更佳，出队时尽量缩减窗口,没有保存在队列里的数都是不用考虑的，因为队列每次入队一个数都需要弹出比入队元素小的元素，那就意味着如果这个元素保存在队列里，后面不会有比这个元素更小的数了，因为如果后面入队更小的数，那前一个数一定会弹出，那这前一个数就不会保存在队列里了
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        cum = [0] + [*itertools.accumulate(A)]
        q = collections.deque()
        ans = len(cum)
        q.append(0)
        for i, num in enumerate(cum[1:], 1):
            flag = -1
            while q and num <= cum[q[-1]]:
                q.pop()
            q.append(i)
            while q and cum[q[0]] + K <= num:
                flag = q.popleft()
            if flag >= 0:
                ans = min(ans, i - flag)
        return ans if ans < len(cum) else -1


Solution().shortestSubarray([84,-37,32,40,95], 167)
