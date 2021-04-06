'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = list(range(1, n + 1))
        res = []

        def dfs(l1, l2, k):
            if k == 0:
                res.append(l2)
            else:
                for i in range(len(l1)):
                    dfs(l1[i + 1:], l2 + [l1[i]], k - 1)  # 避免重复，非重复写法 dfs(l1[:i]+l1[i + 1:], l2 + [l1[i]], k - 1)

        dfs(l, [], k)
        return res


Solution().combine(4, 4)
