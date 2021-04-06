'''数组 A 是 [0, 1, ..., N - 1] 的一种排列，N 是数组 A 的长度。全局倒置指的是 i,j 满足 0 <= i < j < N 并且 A[i] > A[j] ，局部倒置指的是 i 满足 0 <= i < N 并且 A[i] > A[i+1] 。

当数组 A 中全局倒置的数量等于局部倒置的数量时，返回 true 。

 

示例 1:

输入: A = [1,0,2]
输出: true
解释: 有 1 个全局倒置，和 1 个局部倒置。
示例 2:

输入: A = [1,2,0]
输出: false
解释: 有 2 个全局倒置，和 1 个局部倒置。
注意:

A 是 [0, 1, ..., A.length - 1] 的一种排列
A 的长度在 [1, 5000]之间
这个问题的时间限制已经减少了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/global-and-local-inversions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 5 3 4     100 58 140 110 123
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        if len(A) < 2:
            return True
        ma = A[0]
        cnt = 2 if A[0] > A[1] else 1
        for i in range(2, len(A)):
            if A[i] < A[i - 1]:
                cnt += 1
                if cnt > 2:
                    return False
                if A[i] < ma:
                    return False
                ma = A[i - 1]
            else:
                if A[i] < ma:
                    return False
                ma = max(A[i - 1], ma)
                cnt = 1
        return True


Solution().isIdealPermutation([0, 2, 3, 1])
