# 我们有一组排序的数字 D，它是 {'1','2','3','4','5','6','7','8','9'} 的非空子集。（请注意，'0' 不包括在内。）
#
#  现在，我们用这些数字进行组合写数字，想用多少次就用多少次。例如 D = {'1','3','5'}，我们可以写出像 '13', '551', '13513
# 15' 这样的数字。
#
#  返回可以用 D 中的数字写出的小于或等于 N 的正整数的数目。
#
#
#
#  示例 1：
#
#  输入：D = ["1","3","5","7"], N = 100
# 输出：20
# 解释：
# 可写出的 20 个数字是：
# 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
#
#
#  示例 2：
#
#  输入：D = ["1","4","9"], N = 1000000000
# 输出：29523
# 解释：
# 我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
# 81 个四位数字，243 个五位数字，729 个六位数字，
# 2187 个七位数字，6561 个八位数字和 19683 个九位数字。
# 总共，可以使用D中的数字写出 29523 个整数。
#
#
#
#  提示：
#
#
#  D 是按排序顺序的数字 '1'-'9' 的子集。
#  1 <= N <= 10^9
#
#  Related Topics 数学 动态规划
#  👍 66 👎 0

from typing import List

# 数位动态规划，数位dp
import bisect


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        k = len(s)
        D = len(digits)
        dp = [0] * k + [1]
        for i in range(k - 1, -1, -1):
            a = s[i]
            x = bisect.bisect_left(digits, a)
            if x == D:
                dp[i] = x * D ** (k - 1 - i)
                continue
            if digits[x] == a:
                dp[i] += dp[i + 1]
            dp[i] += x * D ** (k - 1 - i)  # digits[x]>a则无需加上dp[i+1]
        return dp[0] + sum(D ** i for i in range(1, k))


Solution().atMostNGivenDigitSet(["7"], 8)


# 2 数学法 类二进制 数位映射
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        k = len(s)
        D = len(digits)
        res = []
        for i, val in enumerate(s):
            x = bisect.bisect_left(digits, val)
            if x == D:
                res.extend([D] * (k - i))
                break
            elif x > 0:
                if digits[x] > val:
                    res.append(x)
                    res.extend([D] * (k - i - 1))
                    break
                else:
                    res.append(x + 1)
            elif x == 0:
                if digits[x] == val:
                    res.append(x + 1)
                else:
                    flag = 1
                    for j in range(len(res) - 1, -1, -1):
                        if res[j] > 0:
                            res[j] -= 1
                            flag = 0
                            break
                    res.extend([D] * (k - i - flag))
                    break
        ans = 0
        for x in res:
            ans = ans * D + x
        return ans


Solution().atMostNGivenDigitSet(["1", "7"], 231)
