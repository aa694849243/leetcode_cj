# 一只猫和一只老鼠在玩一个叫做猫和老鼠的游戏。 
# 
#  它们所处的环境设定是一个 rows x cols 的方格 grid ，其中每个格子可能是一堵墙、一块地板、一位玩家（猫或者老鼠）或者食物。 
# 
#  
#  玩家由字符 'C' （代表猫）和 'M' （代表老鼠）表示。 
#  地板由字符 '.' 表示，玩家可以通过这个格子。 
#  墙用字符 '#' 表示，玩家不能通过这个格子。 
#  食物用字符 'F' 表示，玩家可以通过这个格子。 
#  字符 'C' ， 'M' 和 'F' 在 grid 中都只会出现一次。 
#  
# 
#  猫和老鼠按照如下规则移动： 
# 
#  
#  老鼠 先移动 ，然后两名玩家轮流移动。 
#  每一次操作时，猫和老鼠可以跳到上下左右四个方向之一的格子，他们不能跳过墙也不能跳出 grid 。 
#  catJump 和 mouseJump 是猫和老鼠分别跳一次能到达的最远距离，它们也可以跳小于最大距离的长度。 
#  它们可以停留在原地。 
#  老鼠可以跳跃过猫的位置。 
#  
# 
#  游戏有 4 种方式会结束： 
# 
#  
#  如果猫跟老鼠处在相同的位置，那么猫获胜。 
#  如果猫先到达食物，那么猫获胜。 
#  如果老鼠先到达食物，那么老鼠获胜。 
#  如果老鼠不能在 1000 次操作以内到达食物，那么猫获胜。 
#  
# 
#  给你 rows x cols 的矩阵 grid 和两个整数 catJump 和 mouseJump ，双方都采取最优策略，如果老鼠获胜，那么请你返回 
# true ，否则返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
# 输出：true
# 解释：猫无法抓到老鼠，也没法比老鼠先到达食物。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：grid = ["M.C...F"], catJump = 1, mouseJump = 4
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 输入：grid = ["M.C...F"], catJump = 1, mouseJump = 3
# 输出：false
#  
# 
#  示例 4： 
# 
#  
# 输入：grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
# 输出：false
#  
# 
#  示例 5： 
# 
#  
# 输入：grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 
# 1
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == grid.length 
#  cols = grid[i].length 
#  1 <= rows, cols <= 8 
#  grid[i][j] 只包含字符 'C' ，'M' ，'F' ，'.' 和 '#' 。 
#  grid 中只包含一个 'C' ，'M' 和 'F' 。 
#  1 <= catJump, mouseJump <= 8 
#  
# 
#  Related Topics 图 拓扑排序 记忆化搜索 数组 数学 动态规划 博弈 矩阵 👍 155 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import deque


MOUSE_TURN = 0
CAT_TURN = 1
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
UNKNOW = 0
MOUSE_WIN = 1
CAT_WIN = 2

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        R, C = len(grid), len(grid[0])

        def get_pos(i, j):
            return i * C + j

        banned = set()
        #  制作初始位点
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 'M':
                    mouse_start = get_pos(r, c)
                elif grid[r][c] == 'C':
                    cat_start = get_pos(r, c)
                elif grid[r][c] == 'F':
                    food = get_pos(r, c)
                elif grid[r][c] == '#':
                    banned |= {get_pos(r, c)}

        total = R * C
        degrees = [[[0, 0] for _ in range(total)] for _ in range(total)]
        # degrees[mouse][cat][turn]代表当回合（turn)结束时，mouse和cat的位置
        for mouse in range(total):
            if mouse in banned:
                continue
            for cat in range(total):
                if cat in banned:
                    continue
                mr, mc = divmod(mouse, C)
                cr, cc = divmod(cat, C)
                degrees[mouse][cat][MOUSE_TURN] += 1
                degrees[mouse][cat][CAT_TURN] += 1
                for dr, dc in dirs:
                    nr, nc = mr + dr, mc + dc
                    jump = 1
                    while 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#' and jump <= mouseJump:
                        # degrees[get_pos(nr, nc)][cat][MOUSE_TURN] += 1
                        degrees[mouse][cat][MOUSE_TURN]+=1
                        nr, nc = nr + dr, nc + dc
                        jump += 1
                    nr, nc = cr + dr, cc + dc
                    jump = 1
                    while 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#' and jump <= catJump:
                        # degrees[mouse][get_pos(nr, nc)][CAT_TURN] += 1
                        degrees[mouse][cat][CAT_TURN]+=1
                        nr, nc = nr + dr, nc + dc
                        jump += 1
        status = [[[[UNKNOW, UNKNOW], [UNKNOW, UNKNOW]] for _ in range(total)] for _ in range(total)]
        q = deque()
        for pos in range(total):
            if pos in banned:
                continue
            # 猫与老鼠同一位置，则猫获胜,注意当都处于食物状态时，如果下回合是老鼠回合说明老鼠先到达食物，而老鼠先到达食物的情况一定会被老鼠获胜的状态先遍历到
            status[pos][pos][MOUSE_TURN][0] = CAT_WIN
            status[pos][pos][MOUSE_TURN][1] = 0
            status[pos][pos][CAT_TURN][0] = CAT_WIN
            status[pos][pos][CAT_TURN][1] = 0
            q.append((pos, pos, MOUSE_TURN))
            q.append((pos, pos, CAT_TURN))
            if food != pos:
                # 猫吃到食物获胜
                status[pos][food][MOUSE_TURN][0] = CAT_WIN
                status[pos][food][MOUSE_TURN][1] = 0
                status[pos][food][CAT_TURN][0] = CAT_WIN
                status[pos][food][CAT_TURN][1] = 0
                q.append((pos, food, MOUSE_TURN))
                q.append((pos, food, CAT_TURN))
                # 老鼠吃到食物获胜
                status[food][pos][MOUSE_TURN][0] = MOUSE_WIN
                status[food][pos][MOUSE_TURN][1] = 0
                status[food][pos][CAT_TURN][0] = MOUSE_WIN
                status[food][pos][CAT_TURN][1] = 0
                q.append((food, pos, MOUSE_TURN))
                q.append((food, pos, CAT_TURN))

        def get_pre_status(mouse, cat, turn):
            pre_turn = 1 - turn
            pre_status = [(mouse, cat, pre_turn)]  # 不动状态
            if pre_turn == MOUSE_TURN:
                mr, mc = divmod(mouse, C)
                for dr, dc in dirs:
                    nr, nc = mr + dr, mc + dc
                    jump = 1
                    while 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#' and jump <= mouseJump:
                        pre_status.append((get_pos(nr, nc), cat, pre_turn))
                        jump += 1
                        nr, nc = nr + dr, nc + dc
            else:
                cr, cc = divmod(cat, C)
                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc
                    jump = 1
                    while 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#' and jump <= catJump:
                        pre_status.append((mouse, get_pos(nr, nc), pre_turn))
                        jump += 1
                        nr, nc = nr + dr, nc + dc
            return pre_status

        while q:
            mouse, cat, turn = q.popleft()
            # print(mouse,cat,turn)
            result = status[mouse][cat][turn][0]
            moves = status[mouse][cat][turn][1]
            # print(sorted(get_pre_status(mouse, cat, turn)))
            for pre_mouse, pre_cat, pre_turn in get_pre_status(mouse, cat, turn):
                if status[pre_mouse][pre_cat][pre_turn][0] == UNKNOW:
                    if result == CAT_WIN and pre_turn == CAT_TURN or result == MOUSE_WIN and pre_turn == MOUSE_TURN:
                        status[pre_mouse][pre_cat][pre_turn][0] = result
                        status[pre_mouse][pre_cat][pre_turn][1] = moves + 1
                        q.append((pre_mouse, pre_cat, pre_turn))
                    else:
                        degrees[pre_mouse][pre_cat][pre_turn] -= 1
                        if degrees[pre_mouse][pre_cat][pre_turn] == 0:
                            result =CAT_WIN if pre_turn==MOUSE_TURN else MOUSE_WIN
                            status[pre_mouse][pre_cat][pre_turn][0] = result
                            status[pre_mouse][pre_cat][pre_turn][1] = moves + 1
                            q.append((pre_mouse, pre_cat, pre_turn))
        return status[mouse_start][cat_start][MOUSE_TURN][0] == MOUSE_WIN and status[mouse_start][cat_start][MOUSE_TURN][1] <= 1000

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().canMouseWin(["C.F",".M."], catJump = 1, mouseJump = 2))