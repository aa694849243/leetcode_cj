'''给定一个正整数 n，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 109 + 7的值。

学生出勤记录是只包含以下三个字符的字符串：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果记录不包含多于一个'A'（缺勤）或超过两个连续的'L'（迟到），则该记录被视为可奖励的。

示例 1:

输入: n = 2
输出: 8
解释：
有8个长度为2的记录将被视为可奖励：
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
只有"AA"不会被视为可奖励，因为缺勤次数超过一次。
注意：n 的值不会超过100000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/student-attendance-record-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# https://leetcode-cn.com/problems/student-attendance-record-ii/solution/xue-sheng-chu-qin-ji-lu-ii-by-leetcode/
# 状态转移类题目
# 1动态规划 超时
# f[i] = 2f[i-1] + f[i-4]
class Solution:
    def checkRecord(self, n: int) -> int:
        f = [0] * n + [0] if n > 3 else [0, 0, 0, 0]
        f[0] = 1
        f[1] = 2
        f[2] = 4
        f[3] = 7
        for i in range(4, n + 1):
            f[i] = (2 * f[i - 1] - f[i - 4]) % (10 ** 9 + 7)
        cnt = f[n] % (10 ** 9 + 7)  # 没有A的情况
        for i in range(1, n + 1):
            cnt += (f[i - 1] * f[n - i]) % (10 ** 9 + 7)
        return cnt % (10 ** 9 + 7)


# 2状态转移
class Solution:
    def checkRecord(self, n: int) -> int:
        M = 10 ** 9 + 7
        a0l0 = 1  # a的数量和尾部l的数量
        a1l0 = 1
        a0l1 = 1
        a0l2 = 0  # 总共两个字符第一次为0
        a1l1 = 0
        a1l2 = 0
        for i in range(1, n):
            a0l0_new = (a0l0 + a0l1 + a0l2) % M  # 增加P字符
            a0l1_new = a0l0 % M # 增加L字符
            a0l2_new = a0l1 % M # 增加L字符
            a1l0_new = (a1l0 + a1l1 + a1l2 + a0l0 + a0l1 + a0l2) % M # 增加P字符
            a1l1_new = a1l0 % M # 增加L字符
            a1l2_new = a1l1 % M # 增加L字符
            a0l0 = a0l0_new # 增加P字符
            a0l1 = a0l1_new # 增加p字符
            a0l2 = a0l2_new
            a1l0 = a1l0_new
            a1l1 = a1l1_new
            a1l2 = a1l2_new
        return (a0l0 + a0l1 + a0l2 + a1l0 + a1l1 + a1l2) % M


Solution().checkRecord(29)
