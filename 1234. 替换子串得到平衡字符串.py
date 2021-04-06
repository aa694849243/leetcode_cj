'''有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。

假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。

 

给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。

你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。

请返回待替换子串的最小可能长度。

如果原字符串自身就是一个平衡字符串，则返回 0。

 

示例 1：

输入：s = "QWER"
输出：0
解释：s 已经是平衡的了。
示例 2：

输入：s = "QQWE"
输出：1
解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
示例 3：

输入：s = "QQQW"
输出：2
解释：我们可以把前面的 "QQ" 替换成 "ER"。
示例 4：

输入：s = "QQQQ"
输出：3
解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。
 

提示：

1 <= s.length <= 10^5
s.length 是 4 的倍数
s 中只含有 'Q', 'W', 'E', 'R' 四种字符

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/replace-the-substring-for-balanced-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 滑动窗口
import collections


class Solution:
    def balancedString(self, s: str) -> int:
        m = collections.Counter(s)
        if m['Q'] == m['E'] == m['W'] == m['R']:
            return 0
        m2 = collections.defaultdict(int)
        for ch in m:
            if m[ch] > len(s) // 4:
                m2[ch] = m[ch] - len(s) // 4
        l = 0
        ans = float('inf')
        m3 = collections.defaultdict(int)
        for i, ch in enumerate(s):
            if ch in m2:
                m3[ch] += 1
            flag = 1
            for ch in m2:
                if m3[ch] < m2[ch]:
                    flag = 0
            if flag == 1:
                while l < i and m3 != m2:
                    if s[l] in m3:
                        if m2[s[l]]==m3[s[l]]:
                            break
                        m3[s[l]] -= 1
                    l += 1
                while l < i and s[l] not in m3:
                    l += 1
                ans = min(ans, i - l + 1)
                m3[s[l]] -= 1
                l+=1
        return ans


Solution().balancedString("WWQQRRRRQRQQ")
