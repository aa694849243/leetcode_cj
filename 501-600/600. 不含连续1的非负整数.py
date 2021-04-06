'''给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。

示例 1:

输入: 5
输出: 5
解释:
下面是带有相应二进制表示的非负整数<= 5：
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
说明: 1 <= n <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# 题解 https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones/solution/bu-han-lian-xu-1de-fei-fu-zheng-shu-by-leetcode/
# 1记忆化递归 超出内存限制
import functools


class Solution:
    def findIntegers(self, num: int) -> int:
        @functools.lru_cache(maxsize=None)
        def rec(i, num, sum, prev):
            if sum > num:
                return 0
            if 1 << i > num:
                return 1
            if prev == 1:
                return rec(i + 1, num, sum, 0)  # 前一位为1，只能添加0
            return rec(i + 1, num, sum + (1 << i), 1) + rec(i + 1, num, sum, 0)

        return rec(0, num, 0, 0)


# 2模拟
class Solution:
    def findIntegers(self, num: int) -> int:
        num_s = bin(num)[2:]
        m = {0: 1, 1: 2}
        lenth = len(num_s)
        if lenth < 2:
            return num + 1
        for i in range(2, lenth + 1):
            m[i] = m[i - 1] + m[i - 2]
        prev = 0
        flag = 1
        ans = 0
        for i in range(lenth):
            if num_s[i] == '1' and prev == 0:
                ans += m[lenth - i - 1]
                prev = 1
            else:
                if num_s[i] == '1' and prev == 1:
                    flag = 0
                    ans += m[lenth - i - 1]
                    break
                prev=0
        return ans + flag


Solution().findIntegers(25)
