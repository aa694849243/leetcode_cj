'''
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k==0:
            return []
        res = []
        l = []
        for i in range(1, 10):
            l.append(i)

        def dfs(k, n, l, ans):
            if not l or n < l[0] or n > sum(l):
                return
            elif k == 1 and n in l:
                ans.append(n)
                res.append(ans)
            else:
                for i in range(len(l)):
                    dfs(k-1,n-l[i],l[i+1:],ans+[l[i]])
        dfs(k,n,l,[])
        return res
k=3;n=9
Solution().combinationSum3(k,n)
