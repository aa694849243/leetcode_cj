'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# 递归
class Solution:
    def getRow(self, rowIndex: int) -> List[List[int]]:
        if rowIndex < 1:
            return []

        def rec(n):
            if n == 1:
                return [1]
            a = [1]
            ans = rec(n - 1)
            for i in range(1, len(ans)):
                a.append(ans[i] + ans[i - 1])
            a.append(1)
            return a

        return rec(rowIndex + 1)


# 一维动态规划
class Solution:
    def getRow(self, rowIndex: int) -> List[List[int]]:
        if rowIndex + 1 < 1:
            return []
        r = [1]
        for i in range(rowIndex):
            r.insert(0, 0)
            for j in range(i):
                r[j] = r[j] + r[j + 1]
        return r


Solution().getRow(3)
