'''给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。

（例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）

返回 A 中好子数组的数目。

 

示例 1：

输入：A = [1,2,1,2,3], K = 2
输出：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
示例 2：

输入：A = [1,2,1,3,4], K = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
 

提示：

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarrays-with-k-different-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
# 恰好为K个=小于等于K个的数目-小于等于(k-1)个的数目
import collections


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if K<1:
            return 0
        def atmost(k, nums):
            m = collections.defaultdict(int)
            ans = 0
            j = 0
            for i in range(len(nums)):
                if m[nums[i]] == 0: k -= 1
                m[nums[i]] += 1
                while k < 0:
                    m[nums[j]] -= 1
                    if m[nums[j]] == 0:
                        k += 1
                    j += 1
                ans += i - j + 1  # 每次累加一个贪心的长度（尽可能长）
            return ans

        return atmost(K, A) - atmost(K - 1, A)
