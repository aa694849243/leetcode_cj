# -*- coding: utf-8 -*-
# 欢迎各位勇者来到力扣城，本次试炼主题为「积木拼接」。
# 勇者面前有 `6` 片积木（厚度均为 1），每片积木的形状记录于二维字符串数组 `shapes` 中，`shapes[i]` 表示第 `i` 片积木，其中
# `1` 表示积木对应位置无空缺，`0` 表示积木对应位置有空缺。
# 例如 `["010","111","010"]` 对应积木形状为
# ![image.png](https://pic.leetcode-cn.com/1616125620-nXMCxX-image.png)
#
# 拼接积木的规则如下：
# - 积木片可以旋转、翻面
# - 积木片边缘必须完全吻合才能拼接在一起
# - **每片积木片 `shapes[i]` 的中心点在拼接时必须处于正方体对应面的中心点**
#
# 例如 `3*3`、`4*4` 的积木片的中心点如图所示（红色点）：
# ![middle_img_v2_c2d91eb5-9beb-4c06-9726-f7dae149d86g.png](https://pic.
# leetcode-cn.com/1650509082-wObiEp-middle_img_v2_c2d91eb5-9beb-4c06-9726-f7dae149d86g.
# png){:height="150px"}
#
# 请返回这 6 片积木能否拼接成一个**严丝合缝的正方体**且每片积木正好对应正方体的一个面。
#
# **注意：**
# - 输入确保每片积木均无空心情况（即输入数据保证对于大小 `N*N` 的 `shapes[i]`，内部的 `(N-2)*(N-2)` 的区域必然均为 1）
# - 输入确保每片积木的所有 `1` 位置均连通
#
# **示例 1：**
#
# > 输入：`shapes = [["000","110","000"],["110","011","000"],["110","011","110"],[
# "000","010","111"],["011","111","011"],["011","010","000"]]`
# >
# > 输出：`true`
# >
# > 解释：
# > ![cube.gif](https://pic.leetcode-cn.com/1616125823-hkXAeN-cube.gif)
#
# **示例 2：**
#
# > 输入：`shapes = [["101","111","000"],["000","010","111"],["010","011","000"],[
# "010","111","010"],["101","111","010"],["000","010","011"]]`
# >
# > 输出：`false`
# >
# > 解释：
# > 由于每片积木片的中心点在拼接时必须处于正方体对应面的中心点，积木片 `["010","011","000"]` 不能作为 `["100","110",
# "000"]` 使用，因此无法构成正方体
#
# **提示：**
# - `shapes.length == 6`
# - `shapes[i].length == shapes[j].length`
# - `shapes[i].length == shapes[i][j].length`
# - `3 <= shapes[i].length <= 10`
#
#  Related Topics 数组 回溯 矩阵
#  👍 5 👎 0
import itertools

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def composeCube(self, shapes: List[List[str]]) -> bool:
        n = len(shapes[0])

        def cal(shape):  # 计算每个形状的空间占用情况,6个面，4个方向，两次翻转
            res = [0] * 48
            for x, y in itertools.product(range(n), range(n)):
                if shape[x][y] != "1":
                    continue
                for turn, (xt, yt) in enumerate([(x, y), (x, n - 1 - y)]):  # 上下翻转
                    for rotate, (xr, yr) in enumerate([(xt, yt), (yt, n - 1 - xt), (n - 1 - xt, n - 1 - yt), (n - 1 - yt, xt)]):  # 中心旋转
                        for side, (xs, ys, zs) in enumerate(
                                [(xr, yr, 0), (xr, yr, n - 1), (xr, 0, yr), (xr, n - 1, yr), (0, xr, yr), (n - 1, xr, yr)]):
                            res[turn * 24 + rotate * 6 + side] |= 1 << (xs * n * n + ys * n + zs)
            return res

        sum_ = 2 * n * n + 2 * n * (n - 2) + 2 * (n - 2) * (n - 2)
        if sum(''.join(shape).count("1") for shape in shapes) != sum_:
            return False
        first = cal(shapes[0])
        dp = {first[0], first[24]}  # 第一个积木可以任意摆放，考虑正反两面
        for shape in shapes[1:]:
            dp = {pre | aft for pre in dp for aft in cal(shape) if pre & aft == 0}  # 两个积木的空间占用不能重叠
        return len(dp) > 0


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().composeCube(
    [["000", "110", "000"], ["110", "011", "000"], ["110", "011", "110"], ["000", "010", "111"], ["011", "111", "011"], ["011", "010", "000"]]
))
