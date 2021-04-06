'''在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。

 

示例：

输入：A = [1,0,1,0,1], S = 2
输出：4
解释：
如下面黑体所示，有 4 个满足题目要求的子数组：
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
 

提示：

A.length <= 30000
0 <= S <= A.length
A[i] 为 0 或 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-subarrays-with-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1 O(n^2)超时
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        l, r = 0, 0
        accum = 0
        ans = 0
        while r < len(A):
            accum += A[r]
            tmp = accum
            if tmp == S:
                ans += 1
            while l < r and tmp - A[l] >= S:
                tmp -= A[l]
                l += 1
                if tmp == S:
                    ans += 1
            l = 0
            r += 1
        return ans


# 2前缀和
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:

        if not A:
            return 0
        presum = [0, A[0]]  # 补一个前缀0以便计算right-left
        for i in range(1, len(A)):
            presum.append(presum[-1] + A[i])
        r = 1
        ans = 0

        def bisec_left(lo, hi, target):  # 找左端点
            while lo < hi:
                mid = (lo + hi) // 2
                if presum[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def bisec_right(lo, hi, target):  # 找右端点
            while lo < hi:
                mid = (lo + hi) // 2
                if target < presum[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        while r < len(A) + 1:
            if presum[r] >= S:
                accum1 = presum[r] - S  # accum1即为所要找的两个端点的位置
                left = bisec_left(0, r, accum1)
                right = bisec_right(0, r, accum1)
                ans += right - left  # r为右边端点的位置，左边端点停在left或right任意位置均可
            r += 1
        return ans


# https://leetcode-cn.com/problems/binary-subarrays-with-sum/solution/he-xiang-tong-de-er-yuan-zi-shu-zu-by-leetcode/
# 3 找连续的1
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        index = [-1] + [i for (i, j) in enumerate(A) if j > 0] + [len(A)]
        ans = 0
        if S == 0:  # 0需要特殊处理
            for i in range(1, len(index)):
                w = index[i] - index[i - 1] - 1
                ans += (w + 1) * w // 2
            return ans
        for i in range(1, len(index) - S):  # 末端为len(index)-2,尾段长度要大于等于S+1
            left = index[i] - index[i - 1]
            right = index[i + S] - index[i + S - 1]
            ans += left * right
        return ans


# 4前缀和
import collections


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        m = collections.Counter()
        presum = [0]
        for i in range(len(A)):
            presum.append(presum[-1] + A[i])
        ans = 0
        for x in presum:
            ans += m[x]
            m[x + S] += 1
        return ans


# 5 三指针

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        sumlo = sumhi = 0
        lhi = llo = 0
        ans = 0
        for i in range(len(A)):
            sumlo += A[i]
            while llo < i and sumlo > S:  # 计算左端点到i的前缀和
                sumlo -= A[llo]
                llo += 1

            sumhi += A[i]  # 计算右端点到i的前缀和
            while lhi < i and (sumhi > S or sumhi == S and not A[lhi]):
                sumhi -= A[lhi]
                lhi += 1
            if sumlo == S:
                ans += lhi - llo + 1

        return ans


Solution().numSubarraysWithSum([0, 1, 1], 2)
