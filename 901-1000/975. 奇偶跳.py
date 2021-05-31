# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List

# 给定一个整数数组 A，你可以从某一起始索引出发，跳跃一定次数。在你跳跃的过程中，第 1、3、5... 次跳跃称为奇数跳跃，而第 2、4、6... 次跳跃称为
# 偶数跳跃。
#
#  你可以按以下方式从索引 i 向后跳转到索引 j（其中 i < j）：
#
#
#  在进行奇数跳跃时（如，第 1，3，5... 次跳跃），你将会跳到索引 j，使得 A[i] <= A[j]，A[j] 是可能的最小值。如果存在多个这样的索引
#  j，你只能跳到满足要求的最小索引 j 上。
#  在进行偶数跳跃时（如，第 2，4，6... 次跳跃），你将会跳到索引 j，使得 A[i] >= A[j]，A[j] 是可能的最大值。如果存在多个这样的索引
#  j，你只能跳到满足要求的最小索引 j 上。
#  （对于某些索引 i，可能无法进行合乎要求的跳跃。）
#
#
#  如果从某一索引开始跳跃一定次数（可能是 0 次或多次），就可以到达数组的末尾（索引 A.length - 1），那么该索引就会被认为是好的起始索引。
#
#  返回好的起始索引的数量。
#
#
#
#  示例 1：
#
#  输入：[10,13,12,14,15]
# 输出：2
# 解释：
# 从起始索引 i = 0 出发，我们可以跳到 i = 2，（因为 A[2] 是 A[1]，A[2]，A[3]，A[4] 中大于或等于 A[0] 的最小值），然
# 后我们就无法继续跳下去了。
# 从起始索引 i = 1 和 i = 2 出发，我们可以跳到 i = 3，然后我们就无法继续跳下去了。
# 从起始索引 i = 3 出发，我们可以跳到 i = 4，到达数组末尾。
# 从起始索引 i = 4 出发，我们已经到达数组末尾。
# 总之，我们可以从 2 个不同的起始索引（i = 3, i = 4）出发，通过一定数量的跳跃到达数组末尾。
#
#
#  示例 2：
#
#  输入：[2,3,1,1,4]
# 输出：3
# 解释：
# 从起始索引 i=0 出发，我们依次可以跳到 i = 1，i = 2，i = 3：
#
# 在我们的第一次跳跃（奇数）中，我们先跳到 i = 1，因为 A[1] 是（A[1]，A[2]，A[3]，A[4]）中大于或等于 A[0] 的最小值。
#
# 在我们的第二次跳跃（偶数）中，我们从 i = 1 跳到 i = 2，因为 A[2] 是（A[2]，A[3]，A[4]）中小于或等于 A[1] 的最大值。A[
# 3] 也是最大的值，但 2 是一个较小的索引，所以我们只能跳到 i = 2，而不能跳到 i = 3。
#
# 在我们的第三次跳跃（奇数）中，我们从 i = 2 跳到 i = 3，因为 A[3] 是（A[3]，A[4]）中大于或等于 A[2] 的最小值。
#
# 我们不能从 i = 3 跳到 i = 4，所以起始索引 i = 0 不是好的起始索引。
#
# 类似地，我们可以推断：
# 从起始索引 i = 1 出发， 我们跳到 i = 4，这样我们就到达数组末尾。
# 从起始索引 i = 2 出发， 我们跳到 i = 3，然后我们就不能再跳了。
# 从起始索引 i = 3 出发， 我们跳到 i = 4，这样我们就到达数组末尾。
# 从起始索引 i = 4 出发，我们已经到达数组末尾。
# 总之，我们可以从 3 个不同的起始索引（i = 1, i = 3, i = 4）出发，通过一定数量的跳跃到达数组末尾。
#
#
#  示例 3：
#
#  输入：[5,1,3,4,2]
# 输出：3
# 解释：
# 我们可以从起始索引 1，2，4 出发到达数组末尾。
#
#
#
#
#  提示：
#
#
#  1 <= A.length <= 20000
#  0 <= A[i] < 100000
#
#  Related Topics 栈 动态规划 Ordered Map
#  👍 105 👎 0
import bisect


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        lg = [(n := len(arr))]
        ll = [n]
        stack = [(arr[-1], n - 1)]  # 递增栈
        for i in range(n - 2, -1, -1):
            p = bisect.bisect_left(stack, (arr[i], i))
            if p == len(stack):
                ll.append(stack[p - 1][1])
                lg.append(n)
            elif p == 0:
                if stack[0][0] == arr[i]:
                    ll.append(stack[0][1])
                    lg.append(stack[0][1])
                else:
                    lg.append(stack[0][1])
                    ll.append(n)
            else:
                if stack[p][0] == arr[i]:
                    ll.append(stack[p][1])
                    lg.append(stack[p][1])
                else:
                    lg.append(stack[p][1])
                    p -= 1
                    while p - 1 >= 0 and stack[p - 1][0] == stack[p][0]:
                        p -= 1
                    ll.append(stack[p][1])
            bisect.insort_left(stack, (arr[i], i))
        lg.reverse()
        ll.reverse()
        dp = [[0, 0] for _ in range(n)]
        for i in range(n):
            dp[i][0] += 1
            if lg[i] < n:
                dp[lg[i]][1] += dp[i][0]
            if ll[i] < n:
                dp[ll[i]][0] += dp[i][1]

        return dp[-1][0] + dp[-1][1]


# 索引单调栈
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        def make(indexes):
            stack = []
            ans = [len(indexes)] * len(indexes)
            for i in indexes:
                while stack and i > stack[-1]:  # 对于相等的情况，小的索引先入栈，一定会连接到右侧等于它值的索引
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        li = sorted(list(range(len(arr))), key=lambda i: arr[i])
        lg = make(li)
        li = sorted(list(range(len(arr))), key=lambda i: -arr[i])
        ll = make(li)
        n=len(arr)
        dp = [[0, 0] for _ in range(n)]
        for i in range(n):
            dp[i][0] += 1
            if lg[i] < n:
                dp[lg[i]][1] += dp[i][0]
            if ll[i] < n:
                dp[ll[i]][0] += dp[i][1]
        return dp[-1][0]+dp[-1][1]

Solution().oddEvenJumps([2, 3, 1, 1, 4])
