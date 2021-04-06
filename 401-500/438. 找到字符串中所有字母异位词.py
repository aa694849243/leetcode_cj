'''给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        m1 = collections.Counter(s[:lp])
        m2 = collections.Counter(p)
        ans = []
        if m1 == m2:
            ans.append(0)
        for i in range(lp, len(s)):
            m1[s[i]] += 1
            m1[s[i - lp]] -= 1
            if m1[s[i - lp]] == 0:
                m1.pop(s[i - lp])
            if m1 == m2:
                ans.append(i - lp + 1)
        return ans


s = "cbaebabacd"
p = "abc"
Solution().findAnagrams(s, p)
