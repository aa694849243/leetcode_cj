# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2022-08-28 18:53 
# ide： PyCharm
# 「力扣挑战赛」场地外，小力组织了一个套玩具的游戏。所有的玩具摆在平地上，`toys[i]` 以 `[xi,yi,ri]` 的形式记录了第 `i` 个玩具的坐
# 标 `(xi,yi)` 和半径 `ri`。小扣试玩了一下，他扔了若干个半径均为 `r` 的圈，`circles[j]` 记录了第 `j` 个圈的坐标 `(xj,
# yj)`。套圈的规则如下：
# - 若一个玩具被某个圈完整覆盖了（即玩具的任意部分均在圈内或者圈上），则该玩具被套中。
# - 若一个玩具被多个圈同时套中，最终仅计算为套中一个玩具
#
# 请帮助小扣计算，他成功套中了多少玩具。
#
# **注意：**
# - 输入数据保证任意两个玩具的圆心不会重合，但玩具之间可能存在重叠。
#
# **示例 1：**
#
# > 输入：`toys = [[3,3,1],[3,2,1]], circles = [[4,3]], r = 2`
# >
# > 输出：`1`
# >
# > 解释： 如图所示，仅套中一个玩具
# > ![image.png](https://pic.leetcode-cn.com/1629194140-ydKiGF-image.png)
#
# **示例 2：**
#
# > 输入：`toys = [[1,3,2],[4,3,1],[7,1,2]], circles = [[1,0],[3,3]], r = 4`
# >
# > 输出：`2`
# >
# > 解释： 如图所示，套中两个玩具
# > ![image.png](https://pic.leetcode-cn.com/1629194157-RiOAuy-image.png)
#
# **提示：**
# - `1 <= toys.length <= 10^4`
# - `0 <= toys[i][0], toys[i][1] <= 10^9`
# - `1 <= circles.length <= 10^4`
# - `0 <= circles[i][0], circles[i][1] <= 10^9`
# - `1 <= toys[i][2], r <= 10`
#
#  Related Topics 几何 数组 哈希表 数学 二分查找 排序 👍 13 👎 0
import collections
from typing import List
import math
import bisect

# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/vFjcfV/solution/pai-xu-er-fen-python-yuan-nei-qie-pan-di-leou/
# 内切圆问题
# 数据范围left=x+c-r, right=x-c+r,up=y+c-r, down=y-c+r
class Solution:
    def circleGame(self, toys: List[List[int]], circles: List[List[int]], r: int) -> int:
        circles.sort()  # 根据x坐标排序
        d = collections.defaultdict(list)
        for x, y in circles:
            d[x].append(y)
        ans = 0
        for toys in toys:
            x, y, c = toys
            if c > r:
                continue
            left = x + c - r
            right = x - c + r
            down = y + c - r
            up = y - c + r
            flag=False
            for x_ in range(left, right + 1):
                if len(d[x_]) > 0:
                    down_bound = bisect.bisect_left(d[x_], down)
                    up_bound = bisect.bisect_right(d[x_], up)
                    for idx in range(down_bound, up_bound):
                        if math.sqrt((x_ - x) ** 2 + (d[x_][idx] - y) ** 2) <= r - c:
                            ans += 1
                            flag=True
                            break
                if flag:
                    break
        return ans
# from math import sqrt
# from collections import defaultdict
# import bisect
# class Solution:
#     def circleGame(self, toys, circles, r: int) -> int:
#         ans = 0
#         dic = defaultdict(list)
#         circles.sort()
#         for c in circles:
#             dic[c[0]].append(c[1])
#         for t in toys:
#             x, y, c = t[0], t[1], t[2]
#             if c > r:
#                 continue
#             left, right = x + c - r, x - c + r
#             up, down = y - c + r, y + c - r
#             flag = 0
#             for i in range(left, right + 1):
#                 #二分找纵坐标范围
#                 if dic[i]:
#                     a = bisect.bisect_left(dic[i], down)
#                     b = bisect.bisect_right(dic[i], up)
#                     for j in range(a, b):
#                         c_j = dic[i][j]
#                         dis = sqrt(abs(x - i) ** 2 + abs(y -c_j) ** 2) + c
#                         if r >= dis:
#                             flag = 1
#                             break
#                     if flag:
#                         ans += 1
#                         break
#         return ans

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().circleGame(toys = [[1,3,2],[4,3,1],[7,1,2]], circles = [[1,0],[3,3]], r = 4))