# 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
#
#  （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）
#
#  示例 1:
#
#  输入: N = 10
# 输出: 9
#
#
#  示例 2:
#
#  输入: N = 1234
# 输出: 1234
#
#
#  示例 3:
#
#  输入: N = 332
# 输出: 299
#
#
#  说明: N 是在 [0, 10^9] 范围内的一个整数。
#  Related Topics 贪心算法
#  👍 174 👎 0


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10:
            return N
        a = list(str(N))
        flag = len(a)
        for i in range(len(a) - 2, -1, -1):
            if a[i] <= a[i +1]:
                continue
            else:
                a[i] = str(int(a[i]) - 1)
                flag = i + 1
        if flag == len(a):
            return N
        a[flag:] = ['9'] * len(a[flag:])
        ans = ''.join(a).strip('0')
        return int(ans)
Solution().monotoneIncreasingDigits(1234)