'''
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

通过次数56,725提交次数91,712

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 单调栈----参考官方----26%---------------------
# https://leetcode-cn.com/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode-solution/
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)
        for i in range(len(T)):
            if not stack or T[stack[-1]] >= T[i]:
                stack.append(i)
            else:
                while stack and T[stack[-1]] < T[i]:
                    x = stack.pop()
                    ans[x] = i - x
                stack.append(i)
        return ans


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Solution().dailyTemperatures(temperatures)
