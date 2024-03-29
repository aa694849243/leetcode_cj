'''给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
 

示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False
 

注意：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = collections.Counter(s1)
        m2 = collections.defaultdict(int)
        l, r = 0, 1
        m2[s2[l]] += 1
        while l < len(s2) and r < len(s2):
            while l < r and m2[s2[l]] > m[s2[l]]:
                m2[s2[l]] -= 1
                if m2[s2[l]] == 0:
                    m2.pop(s2[l])
                l += 1
            if m == m2:
                return True
            m2[s2[r]] += 1
            r += 1
        if m == m2:
            return True
        return False


Solution().checkInclusion("adc", "dcda")
