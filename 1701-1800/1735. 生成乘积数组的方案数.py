import collections, heapq, itertools
from typing import List
# 给你一个二维整数数组 queries ，其中 queries[i] = [ni, ki] 。第 i 个查询 queries[i] 要求构造长度为 ni 、每
# 个元素都是正整数的数组，且满足所有元素的乘积为 ki ，请你找出有多少种可行的方案。由于答案可能会很大，方案数需要对 10⁹ + 7 取余 。
#
#  请你返回一个整数数组 answer，满足 answer.length == queries.length ，其中 answer[i]是第 i 个查询的结果
# 。
#
#
#
#  示例 1：
#
#
# 输入：queries = [[2,6],[5,1],[73,660]]
# 输出：[4,1,50734910]
# 解释：每个查询之间彼此独立。
# [2,6]：总共有 4 种方案得到长度为 2 且乘积为 6 的数组：[1,6]，[2,3]，[3,2]，[6,1]。
# [5,1]：总共有 1 种方案得到长度为 5 且乘积为 1 的数组：[1,1,1,1,1]。
# [73,660]：总共有 1050734917 种方案得到长度为 73 且乘积为 660 的数组。1050734917 对 10⁹ + 7 取余得到 507
# 34910 。
#
#
#  示例 2 ：
#
#
# 输入：queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# 输出：[1,2,3,10,5]
#
#
#
#
#  提示：
#
#
#  1 <= queries.length <= 10⁴
#  1 <= ni, ki <= 10⁴
#
#
#  Related Topics 数组 数学 动态规划 组合数学 数论 👍 34 👎 0
import collections
from typing import List


# 插板法
# https://www.cnblogs.com/justPassBy/p/4600772.html
# https://leetcode.cn/problems/count-ways-to-make-array-with-product/solution/python3-zhuan-hua-cheng-ba-mge-xiang-ton-alj0/
# https://leetcode.cn/problems/count-ways-to-make-array-with-product/solution/zhi-yin-shu-fen-jie-zu-he-shu-xue-cheng-rznyp/
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        # 埃氏筛 收集n以下的质数
        def get_primes(n):
            isprim = [1] * n
            isprim[0] = isprim[1] = 0
            for i in range(2, int(n ** 0.5) + 1):
                if isprim[i]:
                    isprim[i ** 2:n:i] = [0] * len(isprim[i ** 2:n:i])
            prims = []
            for i in range(n):
                if isprim[i]:
                    prims.append(i)
            return prims

        prims = get_primes(101)
        # 费马小定理求逆元组合数
        mod = 10 ** 9 + 7
        fac = [1, 1]
        for i in range(2, 10013):
            fac.append(fac[-1] * i % mod)
        facinv = [pow(f, mod - 2, mod) for f in fac]

        def binom(n, k):
            return fac[n] * facinv[k] % mod * facinv[n - k] % mod

        # 获取质因数
        def get_factors(num):
            C = collections.Counter()
            for p in prims:
                # if num % p == 1:
                #     continue
                while num % p == 0:
                    num //= p
                    C[p] += 1
            if num > 1:
                C[num] += 1
            return C

        res = []
        for space, num in queries:
            factors = get_factors(num)
            ans = 1
            for k, v in factors.items():  # v代表有多少个球,space代表多少个槽
                ans *= binom(space + v - 1, space - 1)
                ans %= mod
            res.append(ans)
        return res


# leetcode submit region end(Prohibit modification and deletion)
