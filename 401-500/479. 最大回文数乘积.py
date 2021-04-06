'''你需要找到由两个 n 位数的乘积组成的最大回文数。

由于结果会很大，你只需返回最大回文数 mod 1337得到的结果。

示例:

输入: 2

输出: 987

解释: 99 x 91 = 9009, 9009 % 1337 = 987

说明:

n 的取值范围为 [1,8]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-palindrome-product
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1迭代法
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        hi = 10 ** n - 1  # 最大的n位数
        lo = 10 ** (n - 1)  # 最小的n位数
        maxfirst = (hi ** 2) // (10 ** n)  # 前半部分最大值
        for first in range(maxfirst, lo - 1, -1):
            palidrome = int(str(first) + str(first)[::-1])
            # 因为palifrom一定能被11整除，所以我们假设其中一个的因数能被11整除，即可以进行11的步长搜索结果
            x = hi // 11 * 11  # 从高往低搜索
            for factor in range(x, lo - 1, -11):
                if palidrome % factor == 0 and lo <= palidrome // factor <= hi:
                    return palidrome % 1337
                if palidrome // factor > hi:
                    break


# 2数学法
# 设因数为X,Y=10^n-i,10^n-j,此时i>=1,j>=1; 设a=i+j; 设回文序列p=X*Y=upper*10^n+lower
# p=X*Y=10^n*10^n-10^n*j-10^n*i+i*j=(10^n-i-j)*10^n+i*j=(10^n-a)*10^n+lower,此时lower=i*j=i*(a-i) 则(i-a/2)^2=0.25*a^2-lower 又因为i,j均为整数，那么2*i-a也一定为整数，所以sqrt(a^2-4lower)一定为整数,那么从a>=2开始，找到以lower为后半部分的回文序列，再筛选符合sqrt(a^2-4lower)为整数的lower和a

class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        a = 2
        hi = 10 ** n - 1
        lo = 10 ** (n - 1)
        while a < 2 * 10 ** n:
            upper = 10 ** n - a
            lower = int(str(upper)[::-1])
            if a ** 2 - 4 * lower >= 0 and (a ** 2 - 4 * lower) ** 0.5 == int((a ** 2 - 4 * lower)**0.5):
                num = int(str(upper)+ str(upper)[::-1])
                return num % 1337
            a += 1


Solution().largestPalindrome(2)
