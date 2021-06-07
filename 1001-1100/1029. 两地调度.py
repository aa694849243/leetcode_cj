# -*- coding: utf-8 -*-
from typing import List


# 公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。
#
#  返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。
#
#
#
#  示例：
#
#  输入：[[10,20],[30,200],[400,50],[30,20]]
# 输出：110
# 解释：
# 第一个人去 A 市，费用为 10。
# 第二个人去 A 市，费用为 30。
# 第三个人去 B 市，费用为 50。
# 第四个人去 B 市，费用为 20。
#
# 最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
#
#
#
#
#  提示：
#
#
#  1 <= costs.length <= 100
#  costs.length 为偶数
#  1 <= costs[i][0], costs[i][1] <= 1000
#
#  Related Topics 贪心算法
#  👍 192 👎 0

# 先假设全部到b城市，从b城市改到a城市成本为A-B
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        ans=0
        for i in range(n):
            ans+=costs[i][0]+costs[i+n][1]
        return ans



Solution().twoCitySchedCost([[70, 311], [74, 927], [732, 711], [126, 583]])
