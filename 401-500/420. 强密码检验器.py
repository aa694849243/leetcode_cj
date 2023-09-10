# 满足以下条件的密码被认为是强密码：
#
#
#  由至少 6 个，至多 20 个字符组成。
#  包含至少 一个小写 字母，至少 一个大写 字母，和至少 一个数字 。
#  不包含连续三个重复字符 (比如 "Baaabb0" 是弱密码, 但是 "Baaba0" 是强密码)。
#
#
#  给你一个字符串 password ，返回 将 password 修改到满足强密码条件需要的最少修改步数。如果 password 已经是强密码，则返回 0
# 。
#
#  在一步修改操作中，你可以：
#
#
#  插入一个字符到 password ，
#  从 password 中删除一个字符，或
#  用另一个字符来替换 password 中的某个字符。
#
#
#
#
#  示例 1：
#
#
# 输入：password = "a"
# 输出：5
#
#
#  示例 2：
#
#
# 输入：password = "aA1"
# 输出：3
#
#
#  示例 3：
#
#
# 输入：password = "1337C0d3"
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= password.length <= 50
#  password 由字母、数字、点 '.' 或者感叹号 '!' 组成
#
#
#  Related Topics 贪心 字符串 堆（优先队列）
#  👍 212 👎 0
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        if not password:
            return 6
        n = len(password)
        al, nl, Al = 0, 0, 0
        for ch in password:
            if ch.isupper():
                Al = 1
            elif ch.islower():
                al = 1
            elif ch.isdigit():
                nl = 1
        t = 1
        m = []
        for i in range(1, n):
            if password[i] == password[i - 1]:
                t += 1
            else:
                if t >= 3:
                    m.append(t)
                t = 1
        if t >= 3:  # m处理所有连续字符超过3的数量
            m.append(t)
        if n < 6:  # 小于6，则可以插入到连续字符中间
            return max(6 - n, 3 - (al + Al + nl))
        elif n <= 20:  # 小于20，不删除任何字符
            tmp = sum(x // 3 for x in m)
            return max(3 - (al + Al + nl), tmp)
        ans = x = 3 - (al + Al + nl)
        m0, m1, m2 = [], [], []
        for i in m:
            if i % 3 == 2:
                heapq.heappush(m2, -i)
            elif i % 3 == 1:
                heapq.heappush(m1, -i)
            else:
                heapq.heappush(m0, -i)
        while x > 0 and len(m1) + len(m2) + len(m0) > 0:  # 优先替换连续字符中的字符
            while len(m2) > 0 and x > 0:  # 先替换余数为2的并字符长度长的，替换一个少三个连续字符
                tmp = -heapq.heappop(m2)  # 替换长的是为了删除的时候可以尽可能让字母种类更多
                x -= 1
                if tmp - 3 >= 3:
                    heapq.heappush(m2, -(tmp - 3))
            if x > 0:  # 再替换余数为2的
                while len(m1) > 0 and x > 0:
                    tmp = -heapq.heappop(m1)
                    x -= 1
                    if tmp - 3 >= 3:
                        heapq.heappush(m1, -(tmp - 3))
            if x > 0:  # 最后替换余数为0的
                while len(m0) > 0 and x > 0:
                    tmp = -heapq.heappop(m0)
                    x -= 1
                    if tmp - 3 >= 3:
                        heapq.heappush(m0, -(tmp - 3))
        if x > 0:  # 当连续字符不够替换时，则删去多余的部分，替换部分总数为ans
            return ans + n - 20
        while n > 20 and len(m0) + len(m1) + len(m2) > 0:
            while len(m0) > 0 and n > 20:  # 先删余数为1的
                tmp = -heapq.heappop(m0)
                ans += 1
                n -= 1
                if tmp - 1 >= 3:
                    heapq.heappush(m2, -(tmp - 1))
            if n == 20:
                break
            while len(m1) > 0 and n > 20:  # 再删余数为1的
                tmp = -heapq.heappop(m1)
                n -= 2
                if n >= 20:
                    ans += 2
                    if tmp - 2 >= 3:
                        heapq.heappush(m2, -(tmp - 2))
                else:
                    ans += 1
                    n += 1
                    if tmp - 1 >= 3:
                        heapq.heappush(m0, -(tmp - 1))
            if n == 20:
                break
            while len(m2) > 0 and n > 20:  # 最后删余数为2的
                tmp = -heapq.heappop(m2)
                n -= 3
                if n >= 20:
                    ans += 3
                    if tmp - 3 >= 3:
                        heapq.heappush(m2, -(tmp - 3))
                elif n == 19:
                    ans += 2
                    n += 1
                    if tmp - 2 >= 3:
                        heapq.heappush(m0, -(tmp - 2))
                else:
                    ans += 1
                    n += 2
                    if tmp - 1 >= 3:
                        heapq.heappush(m1, -(tmp - 1))
        if n > 20:
            return ans + n - 20
        for x in m0:
            ans += (-x) // 3
        for x in m1:
            ans += (-x) // 3
        for x in m2:
            ans += (-x) // 3
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().strongPasswordChecker("aaaabbbbccccddeeddeeddeedd")
)
