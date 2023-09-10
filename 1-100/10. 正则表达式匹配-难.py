
# --------------------------------回溯法---------------------------------------------------------------------------------
class Solution:
    @lru_cache
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        first_match = len(s) > 0 and p[0] in ('.', s[0])
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:],p[1:])


# -----------动态规划---------自底向上：填表法--------------------------------------------------------------------------------------
# --https://leetcode-cn.com/problems/regular-expression-matching/solution/tong-guo-dong-tu-jian-ming-jiang-jie-hui-su-he-don/
# https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        matrix = [[False] * (n + 1) for _ in range(m + 1)]
        matrix[-1][-1] = True
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = i != m and p[j] in (s[i], '.')
                if j + 1 < n and p[j+1] == '*':
                    matrix[i][j] = matrix[i][j + 2] or first_match and matrix[i + 1][j]
                else:
                    matrix[i][j] = first_match and matrix[i + 1][j + 1]
        return matrix[0][0]


# ------------动态规划------------自顶向下------------------------------------------------------------------------------------
def isMatch(s: str, p: str) -> bool:
    memo = {}  # 从空表加东西

    def match(j, i):

        if (j, i) not in memo:  # 如果不在则向下搜索
            if j == len(p):  # j匹配到了尽头，i一定要进入尽头才为真，尽头处代表空值
                ans = i == len(s)
            else:
                if j + 1 < len(p) and p[j + 1] == '*':
                    ans = match(j + 2, i) or (p[j] in ('.', s[i]) and i < len(s))
                else:
                    ans = (i < len(s) and p[j] in ('.', s[i])) and match(j + 1, i + 1)
            memo[j, i] = ans

        return memo[j, i]

    return match(0, 0)


s = 'aa'
p = 'a'
isMatch(s, p)
