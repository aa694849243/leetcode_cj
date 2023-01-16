# -*- coding: utf-8 -*-
# 小力正在通过残局练习来备战「力扣挑战赛」中的「五子棋」项目，他想请你能帮他预测当前残局的输赢情况。棋盘中的棋子分布信息记录于二维数组 `pieces` 中，
# 其中 `pieces[i] = [x,y,color]` 表示第 `i` 枚棋子的横坐标为 `x`，纵坐标为 `y`，棋子颜色为 `color`(`0` 表示黑
# 棋，`1` 表示白棋)。假如黑棋先行，并且黑棋和白棋都按最优策略落子，请你求出当前棋局在三步（按 **黑、白、黑** 的落子顺序）之内的输赢情况（三步之内先构成
# 同行、列或对角线连续同颜色的至少 5 颗即为获胜）：
# - 黑棋胜, 请返回 `"Black"`
# - 白棋胜, 请返回 `"White"`
# - 仍无胜者, 请返回 `"None"`
#
# **注意：**
# - 和传统的五子棋项目不同，「力扣挑战赛」中的「五子棋」项目 **不存在边界限制**，即可在 **任意位置** 落子；
# - 黑棋和白棋均按 3 步内的输赢情况进行最优策略的选择
# - 测试数据保证所给棋局目前无胜者；
# - 测试数据保证不会存在坐标一样的棋子。
#
# **示例 1：**
#
# > 输入：
# > `pieces = [[0,0,1],[1,1,1],[2,2,0]]`
# >
# > 输出：`"None"`
# >
# > 解释：无论黑、白棋以何种方式落子，三步以内都不会产生胜者。
#
# **示例 2：**
#
# > 输入：
# > `pieces = [[1,2,1],[1,4,1],[1,5,1],[2,1,0],[2,3,0],[2,4,0],[3,2,1],[3,4,0],[
# 4,2,1],[5,2,1]]`
# >
# > 输出：`"Black"`
# >
# > 解释：三步之内黑棋必胜，以下是一种可能的落子情况：
# > ![902b87df29998b1c181146c8fdb3a4b6.gif](https://pic.leetcode-cn.com/16298006
# 39-KabOfY-902b87df29998b1c181146c8fdb3a4b6.gif)
#
# **提示：**
# - `0 <= pieces.length <= 1000`
# - `pieces[i].length = 3`
# - `-10^9 <= pieces[i][0], pieces[i][1] <=10^9`
# - `0 <= pieces[i][2] <=1`
#
#  Related Topics 数组 数学 枚举 博弈
#  👍 9 👎 0
import collections

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/fsa7oZ/solution/xiang-dui-qing-xi-jian-ji-yi-dian-de-xie-wwi4/
class Solution:
    def gobang(self, pieces: List[List[int]]) -> str:
        dirs = [(1, 0), (0, 1), (1, 1), (1, -1)]  # 四个方向，都是前进的方向
        g = {}
        for x, y, c in pieces:
            g[x, y] = c

        def find_lack(color):
            lines = collections.defaultdict(list)
            for x, y in g:
                if g[x, y] != color: continue
                for k in range(3):  # 最多落下两颗棋子
                    for i, (dx, dy) in enumerate(dirs):
                        head_x, head_y = x - dx * k, y - dy * k  # 起点
                        if (head_x, head_y, i) in lines: continue  # 保存位置和方向
                        for cnt in range(5):
                            nx, ny = head_x + dx * cnt, head_y + dy * cnt
                            c = g.get((nx, ny), -1)
                            if c != color:
                                if c >= 0 or len(lines[head_x, head_y, i]) >= 2:
                                    lines[head_x, head_y, i].clear()  # 占位去重
                                    break
                                lines[head_x, head_y, i].append((nx, ny))
            res = collections.defaultdict(list)
            for (x, y, i), line in lines.items():
                if len(line) == 1 or len(line) == 2:
                    res[len(line)].append(line)  # 保存缺1个和缺2个的线段
            return res

        lines_black = find_lack(0)
        if len(lines_black[1]) > 0: return "Black"  # 缺1个黑色，黑方直接赢
        lines_white = find_lack(1)  # 缺1个白色的线段
        lines_white_set = set(pair[0] for pair in lines_white[1])
        if len(lines_white_set) > 1: return "White"  # 存在多个白色位点可以制造五连,白方赢
        if len(lines_white_set) == 1:  # 只有一个白色位点可以制造五连，必须堵上
            x, y = lines_white_set.pop()
            g[x, y] = 0  # 黑方堵
            lines_black = find_lack(0)
            lines_black_set = set(pair[0] for pair in lines_black[1])
            if len(lines_black_set) > 1: return "Black"  # 黑方堵住后有多个四连，黑方赢
            return "None"  # 黑方堵住后只有一个四连，无法赢
        # 假设黑方无法一步取胜，白方也无法一步取胜的情况
        lines_black_set2 = set((pair[0], pair[1]) for pair in lines_black[2])  # 黑方缺两个的线段，去重
        visted = set()
        for pos0, pos1 in lines_black_set2:
            if pos0 in visted or pos1 in visted: return "Black"  # 黑方缺两个点的线段，有缺点为公共点，直接补上公共点则造成双四连，黑方赢
            visted.add(pos0)
            visted.add(pos1)
        return "None"


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().gobang([[1, 2, 1], [1, 4, 1], [1, 5, 1], [2, 1, 0], [2, 3, 0], [2, 4, 0], [3, 2, 1], [3, 4, 0], [4, 2, 1], [5, 2, 1]]))
