'''对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。

以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

 

示例 1：

输入："13"
输出："3"
解释：13 的 3 进制是 111。
示例 2：

输入："4681"
输出："8"
解释：4681 的 8 进制是 11111。
示例 3：

输入："1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。
 

提示：

n的取值范围是 [3, 10^18]。
输入总是有效且没有前导 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-good-base
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1数学
# https://leetcode-cn.com/problems/smallest-good-base/solution/shu-xue-fang-fa-fen-xi-dai-ma-by-zerotrac/
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)

        def check(k, s, n):
            x = 0
            while s >= 0:
                x += k ** s
                s -= 1
            if x == n:
                return True
            return False
        ans = n - 1
        for s in range(59, 1, -1):
            k = int(n ** (1 / s))
            if k>=2 and check(k, s, n):
                ans = k
                break
        return str(ans)
Solution().smallestGoodBase(22)