#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 一群朋友在度假期间会相互借钱。比如说，小爱同学支付了小新同学的午餐共计 10 美元。如果小明同学支付了小爱同学的出租车钱共计 5 美元。我们可以用一个三元组 (x, y, z) 表示一次交易，表示 x 借给 y 共计 z 美元。用 0, 1, 2 表示小爱同学、小新同学和小明同学（0, 1, 2 为人的标号），上述交易可以表示为 [[0, 1, 10], [2, 0, 5]]。
#
# 给定一群人之间的交易信息列表，计算能够还清所有债务的最小次数。
#
# 注意：
#
# 一次交易会以三元组 (x, y, z) 表示，并有 x ≠ y 且 z > 0。
# 人的标号可能不是按顺序的，例如标号可能为 0, 1, 2 也可能为 0, 2, 6。
#  
#
# 示例 1：
#
# 输入：
# [[0,1,10], [2,0,5]]
#
# 输出：
# 2
#
# 解释：
# 人 #0 给人 #1 共计 10 美元。
# 人 #2 给人 #0 共计 5 美元。
#
# 需要两次交易。一种方式是人 #1 分别给人 #0 和人 #2 各 5 美元。
#  
#
# 示例 2：
#
# 输入：
# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
#
# 输出：
# 1
#
# 解释：
# 人 #0 给人 #1 共计 10 美元。Person #0 gave person #1 $10.
# 人 #1 给人 #0 共计 1 美元。Person #1 gave person #0 $1.
# 人 #1 给人 #2 共计 5 美元。Person #1 gave person #2 $5.
# 人 #2 给人 #0 共计 5 美元。Person #2 gave person #0 $5.
#
# 因此，人 #1 需要给人 #0 共计 4 美元，所有的债务即可还清。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/optimal-account-balancing
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        g = collections.defaultdict(int)
        for a, b, c in transactions:
            g[a] += c
            g[b] -= c
        m = list(g.keys())
        n = len(m)
        self.res = float('inf')

        def dfs(i, count):
            if count >= self.res:
                return
            if i == n:
                self.res = min(self.res, count)
                return
            if g[m[i]] == 0:
                dfs(i + 1, count)
            else:
                for j in range(i + 1, n):
                    if g[m[i]] * g[m[j]] < 0:
                        g[m[j]] += g[m[i]]  # 将i的债务或财富全部转移给j，观察结果,就是4块钱转给-3，-1或全部转给-3再转给-1的次数是一样的
                        dfs(i + 1, count + 1)
                        g[m[j]] -= g[m[i]]

        dfs(0, 0)
        return self.res


Solution().minTransfers([[2, 0, 5], [3, 4, 4]])
