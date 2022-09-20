# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2022-08-25 21:04 
# ide： PyCharm
# 在一条单车道上有 n 辆车，它们朝着同样的方向行驶。给你一个长度为 n 的数组 cars ，其中 cars[i] = [positioni, speedi]
#  ，它表示：
#
#
#  positioni 是第 i 辆车和道路起点之间的距离（单位：米）。题目保证 positioni < positioni+1 。
#  speedi 是第 i 辆车的初始速度（单位：米/秒）。
#
#
#  简单起见，所有车子可以视为在数轴上移动的点。当两辆车占据同一个位置时，我们称它们相遇了。一旦两辆车相遇，它们会合并成一个车队，这个车队里的车有着同样的位置
# 和相同的速度，速度为这个车队里 最慢 一辆车的速度。
#
#  请你返回一个数组 answer ，其中 answer[i] 是第 i 辆车与下一辆车相遇的时间（单位：秒），如果这辆车不会与下一辆车相遇，则
# answer[i] 为 -1 。答案精度误差需在 10⁻⁵ 以内。
#
#
#
#  示例 1：
#
#
# 输入：cars = [[1,2],[2,1],[4,3],[7,2]]
# 输出：[1.00000,-1.00000,3.00000,-1.00000]
# 解释：经过恰好 1 秒以后，第一辆车会与第二辆车相遇，并形成一个 1 m/s 的车队。经过恰好 3 秒以后，第三辆车会与第四辆车相遇，并形成一个 2 m/
# s 的车队。
#
#
#  示例 2：
#
#
# 输入：cars = [[3,4],[5,4],[6,3],[9,1]]
# 输出：[2.00000,1.00000,1.50000,-1.00000]
#
#
#
#
#  提示：
#
#
#  1 <= cars.length <= 10⁵
#  1 <= positioni, speedi <= 10⁶
#  positioni < positioni+1
#
#
#  Related Topics 栈 数组 数学 单调栈 堆（优先队列） 👍 63 👎 0

# https://leetcode.cn/problems/car-fleet-ii/solution/python-dan-diao-zhan-by-qin-qi-shu-hua-2-0k82/
# 后往前遍历单调栈
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        res = []
        cars = cars[::-1]  # 从后往前遍历
        stack = []
        for p, s in cars:
            while stack and stack[-1][1] >= s:  # 速度递增
                stack.pop()
            if not stack:  # 后面的车速全大于当前车速，永远无法追上
                res.append(-1)
                stack.append((p, s, float('inf'))) #追无穷的时间是无穷的
            else:
                while stack and (t := (stack[-1][0] - p) / (s - stack[-1][1])) >= stack[-1][2]:  # 后面的车辆先相撞，不必理会。维护当车与后车相撞时间为最短时间
                    stack.pop()
                stack.append((p, s, t))
                res.append(t)
        return res[::-1]

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().getCollisionTimes([[1,2],[2,1],[4,3],[7,2]]))