'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
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
            for i in range(len(candidates)):
                if i + 1 < range(len(candidates)) and candidates[i] == candidates[i + 1]:
                    continue
                if ans and candidates[i] < ans[-1]:
                    continue
                self.backtrack(candidates[:i] + candidates[i + 1:], sum + candidates[i], target, ans + [candidates[i]])
