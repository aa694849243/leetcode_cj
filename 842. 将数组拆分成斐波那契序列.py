# 给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。
#
#  形式上，斐波那契式序列是一个非负整数列表 F，且满足：
#
#
#  0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
#  F.length >= 3；
#  对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
#
#
#  另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。
#
#  返回从 S 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。
#
#
#
#  示例 1：
#
#  输入："123456579"
# 输出：[123,456,579]
#
#
#  示例 2：
#
#  输入: "11235813"
# 输出: [1,1,2,3,5,8,13]
#
#
#  示例 3：
#
#  输入: "112358130"
# 输出: []
# 解释: 这项任务无法完成。
#
#
#  示例 4：
#
#  输入："0123"
# 输出：[]
# 解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。
#
#
#  示例 5：
#
#  输入: "1101111"
# 输出: [110, 1, 111]
# 解释: 输出 [11,0,11,11] 也同样被接受。
#
#
#
#
#  提示：
#
#
#  1 <= S.length <= 200
#  字符串 S 中只含有数字。
#
#  Related Topics 贪心算法 字符串 回溯算法
#  👍 219 👎 0


from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        lim = 2 ** 31 - 1
        n = len(S)

        def cal(s):
            if len(s)>1 and s[0]=='0':
                return -1
            num = 0
            for i in range(len(s)):
                num *= 10
                num += int(s[i])
                if num > lim:
                    return -1
            return num

        def backtrack(pos):
            num1,num2=ans[-2],ans[-1]
            if num1 + num2 > lim:
                return False
            num = num1 + num2
            ans.append(num)
            if str(num) == S[pos:pos + len(str(num))]:
                if pos + len(str(num)) == n:
                    return True
                else:
                   if backtrack(pos + len(str(num))):
                       return True
            ans.pop()
        for i in range(n - 2):
            x = (n - i - 1) // 2
            for j in range(x + i, i, -1):
                num1, num2 = cal(S[:i + 1]), cal(S[i + 1:j + 1])
                if num1 == -1 or num2 == -1:
                    continue
                ans = [num1, num2]
                if backtrack(j + 1):
                    return ans
        return []


Solution().splitIntoFibonacci('0123')