# -*- coding: utf-8 -*-
import bisect
from typing import List


# n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。
#
#  每 3 个士兵可以组成一个作战单位，分组规则如下：
#
#
#  从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k]
#  作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[
# k] ，其中 0 <= i < j < k < n
#
#
#  请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。
#
#
#
#  示例 1：
#
#
# 输入：rating = [2,5,3,4,1]
# 输出：3
# 解释：我们可以组建三个作战单位 (2,3,4)、(5,4,1)、(5,3,1) 。
#
#
#  示例 2：
#
#
# 输入：rating = [2,1,3]
# 输出：0
# 解释：根据题目条件，我们无法组建作战单位。
#
#
#  示例 3：
#
#
# 输入：rating = [1,2,3,4]
# 输出：4
#
#
#
#
#  提示：
#
#
#  n == rating.length
#  3 <= n <= 1000
#  1 <= rating[i] <= 10^5
#  rating 中的元素都是唯一的
#
#  Related Topics 树状数组 数组 动态规划
#  👍 69 👎 0


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        a = sorted(rating)
        li = [bisect.bisect_left(a, num) + 1 for num in rating]

        def lowbit(num):
            return num & -num

        c = [0] * (2 * len(rating))

        def quiry(num):
            ans = 0
            while num > 0:
                ans += c[num]
                num-=lowbit(num)
            return ans
        def update(num):
            while num<=len(rating):
                c[num]+=1
                num+=lowbit(num)
        rrt=[0]*len(rating)
        rlt=[0]*len(rating)
        n=len(rating)
        for i in range(len(rating)-1,-1,-1):
            num=li[i]
            ltcnt=quiry(num-1)
            rtcnt=n-i-1-ltcnt
            update(num)
            rrt[i],rlt[i]=rtcnt,ltcnt
        c = [0] * (2 * len(rating))
        lrt=[0]*len(rating)
        llt=[0]*len(rating)
        for i in range(len(rating)):
            num=li[i]
            ltcnt=quiry(num-1)
            rtcnt=i-ltcnt
            update(num)
            lrt[i], llt[i] = rtcnt, ltcnt
        ans=0
        for i in range(len(rating)):
            a=lrt[i]*rlt[i]
            b=llt[i]*rrt[i]
            ans+=a+b
        return ans
Solution().numTeams([2,5,3,7,6,8,199])
