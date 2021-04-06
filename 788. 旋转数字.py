'''我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。

如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。

现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？

 

示例：

输入: 10
输出: 4
解释:
在[1, 10]中有四个好数： 2, 5, 6, 9。
注意 1 和 10 不是好数, 因为他们在旋转之后不变。
 

提示：

N 的取值范围是 [1, 10000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotated-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1暴力
class Solution:
    def rotatedDigits(self, N: int) -> int:
        ans = 0
        for i in range(N + 1):
            if set('2569') & set(str(i)) and not (set('347') & set(str(i))):
                ans += 1

        return ans


# 2dp
# 第一个参数i表示原数的第几位，比如i=0就表示第1位(最高位）dp[0]就等于若干个dp[1]的数之和，dp[1]等于若干个dp[2]的数之和，第二个参数equality_flag表示i之前的所有位数是否达到最大值，比如'1234',我们现在在’3‘这个位置，如果equality_flag==true的话说明前面都到达最大数了，也就是前面的数已经是’12‘了，下一个数只能在range(3+1)里面取，而假如前面是’11‘的话，下一个数是可以在range(10)里面取的，第3个参数表示已有的数字里是否有’2569‘
class Solution:
    def rotatedDigits(self, N: int) -> int:
        A = list(map(int, str(N)))
        m = {}

        def dp(i, prefix_max, involution_flag):
            if i == len(A): return +(involution_flag)
            if (i, prefix_max, involution_flag) in m:
                return m[(i, prefix_max, involution_flag)]
            ans = 0
            for j in range(10 if not prefix_max else A[i]+1):
                if j in (3, 4, 7):
                    continue
                ans += dp(i + 1, prefix_max and j == A[i], involution_flag or j in (2, 5, 6, 9))
            m[i, prefix_max, involution_flag] = ans
            return ans

        return dp(0, True, False)


Solution().rotatedDigits(22)
