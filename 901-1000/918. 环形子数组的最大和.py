# 给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。
#
#  在此处，环形数组意味着数组的末端将会与开头相连呈环状。（形式上，当0 <= i < A.length 时 C[i] = A[i]，且当 i >= 0 时
# C[i+A.length] = C[i]）
#
#  此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。（形式上，对于子数组 C[i], C[i+1], ..., C[j]，不存在 i <= k1,
# k2 <= j 其中 k1 % A.length = k2 % A.length）
#
#
#
#  示例 1：
#
#  输入：[1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
#
#
#  示例 2：
#
#  输入：[5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
#
#
#  示例 3：
#
#  输入：[3,-1,2,-1]
# 输出：4
# 解释：从子数组 [2,-1,3] 得到最大和 2 + (-1) + 3 = 4
#
#
#  示例 4：
#
#  输入：[3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
#
#
#  示例 5：
#
#  输入：[-2,-3,-1]
# 输出：-1
# 解释：从子数组 [-1] 得到最大和 -1
#
#
#
#
#  提示：
#
#
#  -30000 <= A[i] <= 30000
#  1 <= A.length <= 30000
#
#  Related Topics 数组
#  👍 157 👎 0

from typing import List

# kadane算法 最大连续子数组和
# 1 右水位线
import itertools
import collections


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(A):
            ans = float('-inf')
            cur = 0
            for x in A:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans

        ans = kadane(A)
        a = [*itertools.accumulate(A[::-1])]
        stack = []
        for num in a:
            if not stack:
                stack.append(num)
            else:
                stack.append(max(num, stack[-1]))
        rightsums_level = stack[::-1]
        leftsums = [*itertools.accumulate(A)]
        for i in range(len(leftsums) - 1):
            ans = max(leftsums[i] + rightsums_level[i + 1], ans)
        return ans


# 2拼接数组+优先队列+单调栈 单调递增
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        ans = max(A)
        A = A + A
        q = collections.deque([0])
        cum = [0] + [*itertools.accumulate(A)]
        for i in range(1, len(cum)):
            while i - q[0] > n:
                q.popleft()
            ans = max(ans, cum[i] - cum[q[0]])
            while q and cum[i] < cum[q[-1]]:
                q.pop()
            q.append(i)
        return ans


# 3两侧区间 循环数组 变换符号
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(A):
            ans = float('-inf')
            cur = 0
            for x in A:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans

        ans1 = kadane(A)
        s = sum(A)
        A = [-num for num in A]
        b = kadane(A[1:])  # 避免全剪掉的情况
        c = kadane(A[:-1])  # 同上
        return max(ans1, s + b, s + c)

# 3两侧区间 循环数组 变换大小规则
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(A):
            ans = float('-inf')
            cur = 0
            for x in A:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans
        a=kadane(A)
        def kadane2(B):
            ans=float('inf')
            cur=0
            for x in B:
                cur=x+min(cur,0)
                ans=min(cur,ans)
            return ans
        b=kadane2(A[1:])
        c=kadane2(A[:-1])
        return max(a,sum(A)-b,sum(A)-c)
Solution().maxSubarraySumCircular([-2,-3,-1])
