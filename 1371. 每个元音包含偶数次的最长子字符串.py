'''给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

 

示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
 

提示：

1 <= s.length <= 5 x 10^5
s 只包含小写英文字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 前缀和+状态压缩
import collections


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        m = [-1] * 32
        m[0] = 0  # 与下面注释呼应
        ans = 0
        flag = 0
        for i in range(len(s)):
            if s[i] == 'a':
                flag ^= 1
            elif s[i] == 'e':
                flag ^= 1 << 1
            elif s[i] == 'i':
                flag ^= 1 << 2
            elif s[i] == 'o':
                flag ^= 1 << 3
            elif s[i] == 'u':
                flag ^= 1 << 4
            if m[
                flag] != -1:  # 这种处理非常巧妙，因为假如最长字符延长到0号位的话是需要+上0号位这个字符的（状态为00000，所有字符都处于偶数状态），对于奇数状态比如'01110'我们需要找到前一个'01110',视作pre later，pre是包含'01110'中三个字符的状态，刚好处于pre_i的那个字符是我们不想要的所以在m['01110']处i要+1
                ans = max(ans, i - m[flag] + 1)
            else:
                m[flag] = i + 1
        return ans


Solution().findTheLongestSubstring("aeoaeoaeo")
