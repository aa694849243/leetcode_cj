# 给出一些不同颜色的盒子
#  boxes ，盒子的颜色由不同的正数表示。
#
#  你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k * k
# 个积分。
#
#  返回 你能获得的最大积分和 。
#
#
#
#  示例 1：
#
#
# 输入：boxes = [1,3,2,2,2,3,4,3,1]
# 输出：23
# 解释：
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 分)
# ----> [1, 3, 3, 3, 1] (1*1=1 分)
# ----> [1, 1] (3*3=9 分)
# ----> [] (2*2=4 分)
#
#
#  示例 2：
#
#
# 输入：boxes = [1,1,1]
# 输出：9
#
#
#  示例 3：
#
#
# 输入：boxes = [1]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= boxes.length <= 100
#  1 <= boxes[i] <= 100
#
#
#  Related Topics 记忆化搜索 数组 动态规划
#  👍 398 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        ma=max(Counter(boxes).values())
        count = []
        boxes_ = [boxes[0]]
        cnt = 1
        for i in range(1, len(boxes)):
            if boxes[i] == boxes[i - 1]:
                cnt += 1
            else:
                count.append(cnt)
                boxes_.append(boxes[i])
                cnt = 1
        count.append(cnt)
        boxes = boxes_
        dp = [[[0] * (ma + 1) for _ in range(len(boxes))] for _ in range(len(boxes))]

        def calc(l, r, k):
            if l > r: return 0
            if dp[l][r][k]: return dp[l][r][k]
            dp[l][r][k] = max(dp[l][r][k], calc(l, r - 1, 0) + (k + count[r]) ** 2)
            for p in range(r - 1, l - 1, -1):
                if boxes[p] == boxes[r]:
                    dp[l][r][k] = max(dp[l][r][k], calc(l, p, k+count[r]) + calc(p + 1, r - 1, 0))
            return dp[l][r][k]

        return calc(0, len(boxes) - 1, 0)


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().removeBoxes([1,2,1,2,1])
)
