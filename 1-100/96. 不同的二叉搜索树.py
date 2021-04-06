'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 卡特兰数
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(i):
                G[i] += G[j] * G[i - j - 1]
        return G[n]

# 数学 卡特兰数
import math
class Solution:
    def numTrees(self, n: int) -> int:
        ans=math.factorial(2*n)/math.factorial(n)**2-math.factorial(2*n)/(math.factorial(n+1)*math.factorial(n-1))
        return ans
#化简
class Solution:
    def numTrees(self, n: int) -> int:
        ans=math.factorial(2*n)/(math.factorial(n)**2*(n+1))
        return int(ans)
#不用math模块
class Solution:
    def numTrees(self, n: int) -> int:
        numerator=1
        denominator=1
        for i in range(1,2*n+1):
            numerator*=i
        for i in range(1,n+1):
            denominator*=i**2
        return int(numerator/(denominator*(n+1)))





