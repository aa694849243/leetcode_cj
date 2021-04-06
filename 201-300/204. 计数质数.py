'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''


# 数学 埃氏筛
# https://leetcode-cn.com/problems/count-primes/solution/pythonzui-you-jie-fa-mei-you-zhi-yi-liao-ba-by-bru/
#时间复杂度O(N*loglogN)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        isprim = [1] * n
        isprim[0] = isprim[1] = 0
        for i in range(2, int(n ** 0.5)+1):
            if isprim[i]:
                isprim[i ** 2:n:i] = [0]*((n-1-i**2)//i+1)
        return sum(isprim)


Solution().countPrimes(10)
