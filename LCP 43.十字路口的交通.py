class Solution:
    def trafficCommand(self, directions: List[str]) -> int:
        status = {}
        status[0, 0] = 0
        status[1, 1] = 0
        status[2, 2] = 0
        status[3, 3] = 0
        status[0, 1] = (1 << 6) | (1 << 8) | (1 << 10) | (1 << 11)
        status[0, 2] = (1 << 2) | (1 << 3) | (1 << 4)
        status[0, 3] = (1 << 0)
        status[1, 0] = (1 << 9)
        status[1, 2] = (1 << 2) | (1 << 5) | (1 << 7) | (1 << 10)
        status[1, 3] = (1 << 0) | (1 << 4) | (1 << 8)
        status[2, 0] = (1 << 7) | (1 << 8) | (1 << 9)
        status[2, 1] = (1 << 11)
        status[2, 3] = (1 << 0) | (1 << 1) | (1 << 3) | (1 << 5)
        status[3, 0] = (1 << 1) | (1 << 4) | (1 << 6) | (1 << 9)
        status[3, 1] = (1 << 3) | (1 << 7) | (1 << 11)
        status[3, 2] = (1 << 2)
        dirs_ = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
        N = [len(x) for x in directions]

        def get_conflicts(status):
            m = {}
            for i in range(4):  # 第0方向
                flag1 = False
                conflict1 = status[0, i]
                for j in range(4):  # 第1方向
                    if conflict1 & status[1, j]:
                        flag2 = True
                    else:
                        flag2 = False
                    conflict2 = conflict1 | status[1, j]
                    for k in range(4):
                        if conflict2 & status[2, k]:
                            flag3 = True
                        else:
                            flag3 = False
                        conflict3 = conflict2 | status[2, k]
                        for v in range(4):
                            if conflict3 & status[3, v]:
                                flag4 = True
                            else:
                                flag4 = False
                            m[(i, j, k, v)] = flag1 or flag2 or flag3 or flag4
            return m

        m = get_conflicts(status)
        # m_ = {key for key in m if not m[key]}
        dp = [[[[float('inf') for _ in range(N[3] + 1)] for _ in range(N[2] + 1)] for _ in range(N[1] + 1)] for _ in range(N[0] + 1)]
        shift = []
        for i in range(1, 1 << 4):
            tmp = []
            for j in range(4):
                if (1 << j) & i:
                    tmp.append(1)
                else:
                    tmp.append(0)
            shift.append(tmp)

        dp[0][0][0][0] = 0
        for i in range(N[0] + 1):
            for j in range(N[1] + 1):
                for k in range(N[2] + 1):
                    for v in range(N[3] + 1):
                        if (i, j, k, v) == (0, 0, 0, 0):
                            continue
                        for di, dj, dk, dv in shift:
                            if i == 0 and di == 1 or j == 0 and dj == 1 or k == 0 and dk == 1 or v == 0 and dv == 1:
                                continue
                            tmp_status = [0, 1, 2, 3]
                            if di == 1:
                                tmp_status[0] = dirs_[directions[0][i - di]]
                                tmp_i = i - di
                            else:
                                tmp_i = i
                            if dj == 1:
                                tmp_status[1] = dirs_[directions[1][j - dj]]
                                tmp_j = j - dj
                            else:
                                tmp_j = j
                            if dk==1:
                                tmp_status[2] = dirs_[directions[2][k - dk]]
                                tmp_k = k - dk
                            else:
                                tmp_k = k
                            if dv == 1:
                                tmp_status[3] = dirs_[directions[3][v - dv]]
                                tmp_v = v - dv
                            else:
                                tmp_v = v
                            if not m[tuple(tmp_status)]:
                                dp[i][j][k][v] = min(dp[i][j][k][v], dp[tmp_i][tmp_j][tmp_k][tmp_v] + 1)
        return dp[-1][-1][-1][-1]


print(Solution().trafficCommand(["N", "W", "S", "E"]))
