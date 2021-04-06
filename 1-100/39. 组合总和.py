'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#-------------caojie--33%------------------------------------------------------------------------------------------------
class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        candidates.sort()
        self.res = []
        ans = []
        self.backtrack(candidates, 0, target, ans)
        return self.res

    def backtrack(self, candidates, sum, target, ans):
        if sum == target:
            self.res.append(ans)
        elif sum > target:
            return
        else:
            for i in candidates:
                if ans and ans[-1] > i:  # 不找之前找过的元素ans[-1]为ans序列中的最大值，我们从小往大遍历，不需要回头找比ans中最大值还小的值
                    continue
                self.backtrack(candidates, sum + i, target, ans + [i])


# class Solution:
#     def combinationSum(self, candidates, target: int):
#         result = []
#         def dfs(temp,res):
#             nonlocal target
#             if temp > target:#剪枝一:当前的总值大于目标值
#                 return
#             if temp == target:#当前值和目标值相等的时候,保存当前结果,并返回
#                 result.append(res[:])
#                 return
#             for i in candidates:
#                 if res and res[-1] > i:#防止重复的方法是,不让其找在当前元素以前的元素
#                     continue
#                 dfs(temp + i, res + [i])
#         dfs(0, [])
#         return result


candidates = [2, 3, 5]
target = 8
Solution().combinationSum(candidates, target)
