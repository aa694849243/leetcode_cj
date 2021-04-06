'''给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k 个积分。
当你将所有盒子都去掉之后，求你能获得的最大积分和。

 

示例：

输入：boxes = [1,3,2,2,2,3,4,3,1]
输出：23
解释：
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 分)
----> [1, 3, 3, 3, 1] (1*1=1 分)
----> [1, 1] (3*3=9 分)
----> [] (2*2=4 分)
 

提示：

1 <= boxes.length <= 100
1 <= boxes[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-boxes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# https://leetcode-cn.com/problems/remove-boxes/solution/yi-chu-he-zi-by-leetcode-solution/
# 动态规划
# 连续的作为一个整体删除一定得分更高
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        dp = [[[0] * len(boxes) for _ in range(len(boxes))] for _ in range(len(boxes))]

        def cal(l, r, k):
            if l > r: return 0
            if dp[l][r][k] != 0: return dp[l][r][k]  # 保存的计算直接出结果
            while r > l and boxes[r] == boxes[r - 1]:  # r>l表示最多只留一个在[l,r]区间中只留一个
                k += 1
                r -= 1
            dp[l][r][k] = cal(l, r - 1, 0) + (k + 1) ** 2
            for i in range(r - 1, l - 1, -1):  # 倒着走更快些，因为更早碰到连续的
                if boxes[i] == boxes[r]:
                    dp[l][r][k] = max(dp[l][r][k], cal(l, i, k + 1) + cal(i + 1, r - 1, 0))
            return dp[l][r][k]

        return cal(0, len(boxes) - 1, 0)


Solution().removeBoxes([1, 1, 1])
