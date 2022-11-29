# -*- coding: utf-8 -*-
# Alice 是 n 个花园的园丁，她想通过种花，最大化她所有花园的总美丽值。
#
#  给你一个下标从 0 开始大小为 n 的整数数组 flowers ，其中 flowers[i] 是第 i 个花园里已经种的花的数目。已经种了的花 不能 移走
# 。同时给你 newFlowers ，表示 Alice 额外可以种花的 最大数目 。同时给你的还有整数 target ，full 和 partial 。
#
#  如果一个花园有 至少 target 朵花，那么这个花园称为 完善的 ，花园的 总美丽值 为以下分数之 和 ：
#
#
#  完善 花园数目乘以 full.
#  剩余 不完善 花园里，花的 最少数目 乘以 partial 。如果没有不完善花园，那么这一部分的值为 0 。
#
#
#  请你返回 Alice 种最多 newFlowers 朵花以后，能得到的 最大 总美丽值。
#
#
#
#  示例 1：
#
#  输入：flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1
# 输出：14
# 解释：Alice 可以按以下方案种花
# - 在第 0 个花园种 2 朵花
# - 在第 1 个花园种 3 朵花
# - 在第 2 个花园种 1 朵花
# - 在第 3 个花园种 1 朵花
# 花园里花的数目为 [3,6,2,2] 。总共种了 2 + 3 + 1 + 1 = 7 朵花。
# 只有 1 个花园是完善的。
# 不完善花园里花的最少数目是 2 。
# 所以总美丽值为 1 * 12 + 2 * 1 = 12 + 2 = 14 。
# 没有其他方案可以让花园总美丽值超过 14 。
#
#
#  示例 2：
#
#  输入：flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6
# 输出：30
# 解释：Alice 可以按以下方案种花
# - 在第 0 个花园种 3 朵花
# - 在第 1 个花园种 0 朵花
# - 在第 2 个花园种 0 朵花
# - 在第 3 个花园种 2 朵花
# 花园里花的数目为 [5,4,5,5] 。总共种了 3 + 0 + 0 + 2 = 5 朵花。
# 有 3 个花园是完善的。
# 不完善花园里花的最少数目为 4 。
# 所以总美丽值为 3 * 2 + 4 * 6 = 6 + 24 = 30 。
# 没有其他方案可以让花园总美丽值超过 30 。
# 注意，Alice可以让所有花园都变成完善的，但这样她的总美丽值反而更小。
#
#
#
#
#  提示：
#
#
#  1 <= flowers.length <= 10⁵
#  1 <= flowers[i], target <= 10⁵
#  1 <= newFlowers <= 10¹⁰
#  1 <= full, partial <= 10⁵
#
#
#  Related Topics 贪心 数组 双指针 二分查找 排序
#  👍 28 👎 0
import bisect
import itertools
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        n = len(flowers)
        idx = bisect.bisect_left(flowers, target)
        ans = full * (n - idx)
        if idx == 0:
            return ans
        flowers = flowers[:idx]
        precums = [*itertools.accumulate(flowers)]
        resi_flowers = [target - num for num in flowers]
        resi_precums = [*itertools.accumulate(resi_flowers[::-1])]
        mi = min(flowers)

        def calc(r, num, cost):
            if l < len(flowers):  # 当l取不完整个序列时，尽可能多的拿完全花园的分数
                # r = bisect.bisect_right(resi_precums[:len(flowers) - l], cost)  # 考虑到交叉情况
                r = min(len(flowers) - l, r)
                if r == 0:  # 完全花园分数一个都拿不到
                    return num * partial
                cost -= resi_precums[r - 1]
                r_num = r + cost // (target - num)
                if r_num >= len(flowers):  # 完全花园可以拿完整个序列时，需要比较是否需要不完全花园的分数
                    r_num = len(flowers)
                    return max(r_num * full, (r_num - 1) * full + partial * num)
                else:
                    return num * partial + r_num * full
            else:  # 当l取完整个序列时，则target-num为铺满一个所需要的耗费花数目
                r_num = cost // (target - num)
                if r_num >= len(flowers):
                    r_num = len(flowers)
                    return max(num * partial + (r_num - 1) * full, r_num * full)
                else:
                    return num * partial + r_num * full

        res = ans
        l = 0
        r = bisect.bisect_right(resi_precums, newFlowers)  # 双指针
        for num in range(mi, target):
            while l < len(flowers) and flowers[l] <= num:  # l代表不完全花园的数目
                l += 1
            cost = newFlowers - l * num + precums[l - 1]
            if cost < 0:
                break
            while r > 0 and resi_precums[r - 1] > cost:  # r代表完全花园的数目
                r -= 1
            tmp = calc(r, num, cost)
            if tmp != -1:
                res = max(ans + tmp, res)
        return res


# leetcode submit region end(Prohibit modification and deletion)


print(Solution().maximumBeauty(
    [965, 344, 315, 867], 1000, 1000, 10, 1))
