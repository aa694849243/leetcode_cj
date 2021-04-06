'''
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

 

示例：

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
 

提示：

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# 动态规划 caojie 44%
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * len(A) for _ in range(len(B))]
        length = 0
        for i in range(len(A)):
            dp[0][i] = int(B[0] == A[i])
            length = max(dp[0][i], length)
        for i in range(len(B)):
            dp[i][0] = int(B[i] == A[0])
            length = max(dp[i][0], length)
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    dp[j][i] = dp[j - 1][i - 1] + 1
                    length = max(length, dp[j][i])
                else:
                    dp[j][i] = 0
        return length


# 滑动窗口
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # 求A，B左对齐右切平，连续最长子数组长度。
        def maxLength(A, B) -> int:
            maxSame = curSame = 0  # 全局最大，当前连续
            for a, b in zip(A, B):
                if a == b:
                    curSame += 1  # 相同连续+1
                else:  # 不同看看maxSame有没破纪录
                    maxSame = max(maxSame, curSame)
                    curSame = 0  # 连续清零
            return max(maxSame, curSame)

        # ★↑ 不能只返回maxSame，否则当真正的maxSame发生在末尾则出错。
        ans = 0
        for ai in range(len(A)):  # 求 A[ai]对齐B[0] 的情况
            ans = max(ans, maxLength(A[ai:], B))
        for bi in range(len(B)):  # A[0]对齐B[0]的已经做过了，故初始bi=1
            ans = max(ans, maxLength(A, B[bi:]))
        return ans


# 作者：java_Lee
# 链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/hua-dong-chuang-kou-12xing-ji-jian-python-by-java_/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# 时间复杂度： O((N+M)×min(N,M))。

# 二分查找+哈希法 哈希表法 Rabin-Karp算法哈希 序列值哈希
pow(10, 3, 50)


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        base, mod = 113, 10 ** 9 + 9

        def check(length: int) -> bool:
            hashA = 0
            for i in range(length):
                hashA = (hashA * base + A[i]) % mod
            bucketA = {hashA}
            mult = pow(base, length - 1, mod)
            for i in range(length, len(A)):
                hashA = ((hashA - A[i - length] * mult) * base + A[i]) % mod
                bucketA.add(hashA)

            hashB = 0
            for i in range(length):
                hashB = (hashB * base + B[i]) % mod
            if hashB in bucketA:
                return True
            for i in range(length, len(B)):
                hashB = ((hashB - B[i - length] * mult) * base + B[i]) % mod
                if hashB in bucketA:
                    return True

            return False

        left, right = 0, min(len(A), len(B))
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / maximum - length - of - repeated - subarray / solution / zui - chang - zhong - fu - zi - shu - zu - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# 时间复杂度：O\big((M+N) \log{(\min(M, N))}\big)O((M+N)log(min(M,N)))。
#
# 空间复杂度：O(N)O(N)。


A = [0, 0, 0, 0, 1]
B = [1, 0, 0, 0, 0]
Solution().findLength(A, B)
