# -*- coding: utf-8 -*-
# 「力扣挑战赛」中有一个由 `N` 个关卡组成的**环形**闯关游戏，关卡编号为 `0`~`N-1`，编号 `0` 的关卡和编号 `N-1` 的关卡相邻。每个
# 关卡均有积分要求，`challenge[i]` 表示挑战编号 `i` 的关卡最少需要拥有的积分。
# ![图片.png](https://pic.leetcode-cn.com/1630392170-ucncVS-%E5%9B%BE%E7%89%87.
# png)
#
# 小扣想要挑战关卡，闯关的具体规则如下：
#
# - 初始小扣可以指定其中一个关卡为「开启」状态，其余关卡将处于「未开启」状态。
# - 小扣可以挑战处于「开启」状态且**满足最少积分要求**的关卡，若小扣挑战该关卡前积分为 `score`，挑战结束后，积分将增长为 `score|
# challenge[i]`（即位运算中的 `"OR"` 运算）
# - 在挑战某个关卡后，该关卡两侧相邻的关卡将会开启（若之前未开启）
#
# 请帮助小扣进行计算，初始最少需要多少积分，可以挑战 **环形闯关游戏** 的所有关卡。
#
# **示例1：**
#
# > 输入：`challenge = [5,4,6,2,7]`
# >
# > 输出：`4`
# >
# > 解释： 初始选择编号 3 的关卡开启，积分为 4
# > 挑战编号 3 的关卡，积分变为 $4 | 2 = 6$，开启 2、4 处的关卡
# > 挑战编号 2 的关卡，积分变为 $6 | 6 = 6$，开启 1 处的关卡
# > 挑战编号 1 的关卡，积分变为 $6 | 4 = 6$，开启 0 处的关卡
# > 挑战编号 0 的关卡，积分变为 $6 | 5 = 7$
# > 挑战编号 4 的关卡，顺利完成全部的关卡
#
# **示例2：**
#
# > 输入：`challenge = [12,7,11,3,9]`
# >
# > 输出：`8`
# >
# > 解释： 初始选择编号 3 的关卡开启，积分为 8
# > 挑战编号 3 的关卡，积分变为 $8 | 3 = 11$，开启 2、4 处的关卡
# > 挑战编号 2 的关卡，积分变为 $11 | 11 = 11$，开启 1 处的关卡
# > 挑战编号 4 的关卡，积分变为 $11 | 9 = 11$，开启 0 处的关卡
# > 挑战编号 1 的关卡，积分变为 $11 | 7 = 15$
# > 挑战编号 0 的关卡，顺利完成全部的关卡
#
# **示例3：**
#
# > 输入：`challenge = [1,1,1]`
# >
# > 输出：`1`
#
# **提示：**
# - `1 <= challenge.length <= 5*10^4`
# - `1 <= challenge[i] <= 10^18`
#
#  Related Topics 位运算 并查集 数组 堆（优先队列）
#  👍 9 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/K8GULz/solution/cong-gao-dao-di-que-ding-da-an-de-er-jin-qvdi/
class Solution:
    def ringGame(self, challenge: List[int]) -> int:
        n = len(challenge)
        n3 = n * 3
        challenge = challenge * 3
        idx_left = [0] * n3
        idx_right = [0] * n3
        left_max_score = [0] * n3
        right_max_score = [0] * n3
        for i in range(n3):
            left_max_score[i] = challenge[i]
            j = i - 1
            while j >= 0 and left_max_score[i] >= challenge[j]:
                left_max_score[i] |= left_max_score[j]
                j = idx_left[j]
            idx_left[i] = j
        for i in range(n3 - 1, -1, -1):
            right_max_score[i] = challenge[i]
            j = i + 1
            while j < n3 and right_max_score[i] >= challenge[j]:
                right_max_score[i] |= right_max_score[j]
                j = idx_right[j]
            idx_right[i] = j

        def check(m):  # 检查m能否通过全部关卡
            st = n
            while st < 2 * n:  # 从第一个关开始检查
                if challenge[st] > m:  # 直接淘汰
                    st += 1
                    continue
                s, l, r = m | left_max_score[st] | right_max_score[st], idx_left[st], idx_right[st]
                while 1:
                    if r - l > n: return True
                    while l >= 0 and s >= challenge[l]:  # 尽量向左延伸
                        s |= left_max_score[l]
                        l = idx_left[l]
                    if s >= challenge[r]:  # 无法右括了，跳出
                        s |= right_max_score[r]
                        r = idx_right[r]
                    else:
                        break
                st = r  # 跳过合并的点
            return False

        m = bit = 1 << (max(challenge).bit_length() - 1)
        while bit:
            bit >>= 1
            if not check(m | (bit - 1)):
                m |= bit
        return m
    # leetcode submit region end(Prohibit modification and deletion)


print(Solution().ringGame([5, 4, 6, 2, 7]))
