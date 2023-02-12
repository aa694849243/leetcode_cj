# -*- coding: utf-8 -*-
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        # 连续数组的原地去重
        ans = 0
        a, i0 = [], -1
        for i, num in enumerate(nums):
            if k % num:
                a = []
                i0 = i
                continue
            a.append([num, i])
            j = 0
            for p in a:  # 原地去重
                p[0] = math.lcm(p[0], num)
                if a[j][0] != p[0]:
                    j += 1
                    a[j] = p
                else:
                    a[j][1] = p[1]  # 保留最后一个，取远的
            del a[j + 1:]
            if a[0][0] == k:
                ans += a[0][1] - i0
        return ans
