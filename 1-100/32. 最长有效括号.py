'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# -----------------------caojie-11%----------------------------------------------------------------------
# 哈希表法--https://leetcode-cn.com/problems/longest-valid-parentheses/solution/shuang-zhi-zhen-ha-xi-biao-fa-by-aa694849243/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        re = {}
        M = 0
        while right < len(s):
            if s[right] == ')':
                if left - 1 < 0:
                    re[right] = -1
                    right += 1
                    left = right
                elif s[left - 1] == '(':
                    left -= 1
                    if left - 1 in re and re[left - 1] != -1:
                        left = re[left - 1]
                    re[right] = left
                    M = max(right - left + 1, M)
                    right += 1
                else:  # s[left-1]==")"的情况
                    left = re[left - 1]
                    re[right] = left
                    if left == -1:
                        right += 1
                        left = right
                        continue
                    M = max(right - left + 1, M)
                    right += 1
            else:
                right += 1
                left = right

        return M

#---动态规划------------------------------------------------------------------------------------------
#--https://leetcode-cn.com/problems/longest-valid-parentheses/solution/xiao-bai-du-neng-kan-dong-de-dong-tai-gui-hua-si-l/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = ' ' + s
        dp = [0 for _ in range(len(s))]
        maxs = 0
        for i in range(1, len(s), 1):
            if s[i] == ')':
                if i - 1 >= 0 and s[i - 1] == '(':
                    # 情况1
                    if i - 1 == 0:
                        dp[i] = 2
                        maxs = max(maxs, dp[i])
                    else:
                        dp[i] = dp[i - 2] + 2
                        maxs = max(maxs, dp[i])
                elif i - 1 >= 0 and s[i - 1] == ')':
                    # 情况2
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                        maxs = max(maxs, dp[i])
        return maxs


Solution().longestValidParentheses(S)
