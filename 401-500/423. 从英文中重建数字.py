'''给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。

注意:

输入只包含小写英文字母。
输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
输入字符串的长度小于 50,000。
示例 1:

输入: "owoztneoer"

输出: "012" (zeroonetwo)
示例 2:

输入: "fviefuro"

输出: "45" (fourfive)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reconstruct-original-digits-from-english
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
import collections


class Solution:
    def originalDigits(self, s: str) -> str:
        m = collections.Counter(s)
        ans = {}
        ans[0] = m['z']
        ans[2] = m['w']
        ans[4] = m['u']
        ans[6] = m['x']
        ans[8] = m['g']
        ans[3] = m['h'] - ans[8]
        ans[5] = m['f'] - ans[4]
        ans[7] = m['s'] - ans[6]
        ans[9] = m['i'] - ans[5] - ans[6] - ans[8]
        ans[1] = m['n'] - ans[7] - 2*ans[9]
        output = [str(key) * ans[key] for key in sorted(ans.keys())]
        return ''.join(output)
Solution().originalDigits("nnei")