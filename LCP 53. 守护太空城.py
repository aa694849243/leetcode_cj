# -*- coding: utf-8 -*-
# 各位勇者请注意，力扣太空城发布陨石雨红色预警。
#
# 太空城中的一些舱室将要受到陨石雨的冲击，这些舱室按照编号 `0 ~ N` 的顺序依次排列。为了阻挡陨石损毁舱室，太空城可以使用能量展开防护屏障，具体消耗如下
# ：
#
# - 选择一个舱室开启屏障，能量消耗为 `2`
# - 选择相邻两个舱室开启联合屏障，能量消耗为 `3`
# - 对于已开启的**一个**屏障，**多维持一时刻**，能量消耗为 `1`
#
# 已知陨石雨的影响范围和到达时刻，`time[i]` 和 `position[i]` 分别表示该陨石的到达时刻和冲击位置。请返回太空舱能够守护所有舱室所需要的
# 最少能量。
#
# **注意：**
# - 同一时间，一个舱室不能被多个屏障覆盖
# - 陨石雨仅在到达时刻对冲击位置处的舱室有影响
#
# **示例 1：**
#
# > 输入：`time = [1,2,1], position = [6,3,3]`
# >
# > 输出：`5`
# >
# > 解释：
# > 时刻 1，分别开启编号 3、6 舱室的屏障，能量消耗 2*2 = 4
# > 时刻 2，维持编号 3 舱室的屏障，能量消耗 1
# > 因此，最少需要能量 5
#
# **示例 2：**
#
# > 输入：`time = [1,1,1,2,2,3,5], position = [1,2,3,1,2,1,3]`
# >
# > 输出：`9`
# >
# > 解释：
# > 时刻 1，开启编号 1、2 舱室的联合屏障，能量消耗 3
# > 时刻 1，开启编号 3 舱室的屏障，能量消耗 2
# > 时刻 2，维持编号 1、2 舱室的联合屏障，能量消耗 1
# > 时刻 3，维持编号 1、2 舱室的联合屏障，能量消耗 1
# > 时刻 5，重新开启编号 3 舱室的联合屏障，能量消耗 2
# > 因此，最少需要能量 9
#
# **提示：**
# + `1 <= time.length == position.length <= 500`
# + `1 <= time[i] <= 5`
# + `0 <= position[i] <= 100`
#
#  Related Topics 位运算 数组 动态规划 状态压缩
#  👍 9 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/EJvmW4/solution/by-endlesscheng-pk2q/
class Solution:
    def defendSpaceCity(self, time: List[int], position: List[int]) -> int:
        n, m = max(position), 1 << max(time)
        p_state = [0] * (n + 1)
        for t, p in zip(time, position):
            p_state[p] |= 1 << (t - 1)

        union = [0] * m  # union[i] 表示i状态，开启的联合屏障花费
        single = [0] * m
        for i in range(1, m):  # 预处理开启联合屏障和单个屏障的状态
            b1 = i & -i
            j = i ^ b1
            b2 = j & -j
            union[i] = union[j] + (1 if b1 == b2 >> 1 else 3)
            single[i] = single[j] + (1 if b1 == b2 >> 1 else 2)
        f = [[float('inf')] * (m) for _ in range(n + 1)]
        for i in range(m):
            f[0][i] = union[i] + single[((m - 1) ^ i) & p_state[0]]
        for i in range(1, n + 1):
            for j in range(m):
                pre = mask = (m - 1) ^ j  # pre代表上一位点开启联合屏障的状态(时间)
                while 1: # pre与j不重合，j固定，每次向下更新pre，增加更多的单个屏障
                    f[i][j] = min(f[i][j], f[i - 1][pre] + union[j] + single[(mask ^ pre) & p_state[i]])
                    if not pre: break
                    pre = (pre - 1) & mask
        return f[n][0] # 最后一个点不用开启联合屏障
# leetcode submit region end(Prohibit modification and deletion)
