# 定义 str = [s, n] 表示 str 由 n 个字符串 s 连接构成。 
# 
#  
#  例如，str == ["abc", 3] =="abcabcabc" 。 
#  
# 
#  如果可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。 
# 
#  
#  例如，根据定义，s1 = "abc" 可以从 s2 = "abdbec" 获得，仅需要删除加粗且用斜体标识的字符。 
#  
# 
#  现在给你两个字符串 s1 和 s2 和两个整数 n1 和 n2 。由此构造得到两个字符串，其中 str1 = [s1, n1]、str2 = [s2, 
# n2] 。 
# 
#  请你找出一个最大整数 m ，以满足 str = [str2, m] 可以从 str1 获得。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s1.length, s2.length <= 100 
#  s1 和 s2 由小写英文字母组成 
#  1 <= n1, n2 <= 10⁶ 
#  
# 
#  Related Topics 字符串 动态规划 
#  👍 184 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        l1, l2 = len(s1), len(s2)
        s1cnt = s2cnt = 0
        m = {}
        idx2 = 0
        while s1cnt < n1:
            s1cnt += 1  # 拿出一个s1进行匹配
            for i in range(l1):
                if s1[i] == s2[idx2]:
                    idx2 += 1
                    if idx2 == l2:
                        s2cnt, idx2 = s2cnt + 1, 0
            if s1cnt == n1:  # 没找到循环节
                return s2cnt // n2
            if idx2 not in m:
                m[idx2] = s1cnt, s2cnt
            else:  # 出现了循环节
                s1cnt_prime, s2cnt_prime = m[idx2]
                loop1, loop2 = (s1cnt - s1cnt_prime), (s2cnt - s2cnt_prime)
                ans = (n1 - s1cnt_prime) // loop1 * loop2 + s2cnt_prime
                resi= (n1 - s1cnt_prime) % loop1
                for _ in range(resi):
                    for i in range(l1):
                        if s1[i] == s2[idx2]:
                            idx2 += 1
                            if idx2 == l2:
                                ans, idx2 = ans + 1, 0
                return ans // n2
# leetcode submit region end(Prohibit modification and deletion)

