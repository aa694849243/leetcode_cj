'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def rec(l1, l2):
            if not l2:
                res.append(l1)
            else:
                for i in range(len(l2)):
                    if i > 0 and l2[i] == l2[i - 1]:
                        continue
                    rec(l1 + [l2[i]], l2[:i] + l2[i + 1:])

        rec([], nums)
        return res
nums=[1,1,2]
Solution().permuteUnique(nums)