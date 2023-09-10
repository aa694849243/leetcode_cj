# 以字符串的形式给出 n , 以字符串的形式返回 n 的最小 好进制 。 
# 
#  如果 n 的 k(k>=2) 进制数的所有数位全为1，则称 k(k>=2) 是 n 的一个 好进制 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = "13"
# 输出："3"
# 解释：13 的 3 进制是 111。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = "4681"
# 输出："8"
# 解释：4681 的 8 进制是 11111。
#  
# 
#  示例 3： 
# 
#  
# 输入：n = "1000000000000000000"
# 输出："999999999999999999"
# 解释：1000000000000000000 的 999999999999999999 进制是 11。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n 的取值范围是 [3, 10¹⁸] 
#  n 没有前导 0 
#  
# 
#  Related Topics 数学 二分查找 
#  👍 166 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n=int(n)
        def check(b, s):
            ans=0
            for i in range(s+1):
                ans+=b**i
            return ans==n

        for s in range(59, 1, -1): # s+1位的二进制
            b = int(n ** (1 / s))
            if b>1 and check(b,s):
                return str(b)
        return str(n - 1)

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().smallestGoodBase("13"))