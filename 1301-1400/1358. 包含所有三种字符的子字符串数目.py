# -*- coding: utf-8 -*-
# 给你一个字符串 s ，它只包含三种字符 a, b 和 c 。
#
#  请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。
#
#
#
#  示例 1：
#
#  输入：s = "abcabc"
# 输出：10
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bc
# abc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
#
#
#  示例 2：
#
#  输入：s = "aaacb"
# 输出：3
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
#
#
#  示例 3：
#
#  输入：s = "abc"
# 输出：1
#
#
#
#
#  提示：
#
#
#  3 <= s.length <= 5 x 10^4
#  s 只包含字符 a，b 和 c 。
#
#  Related Topics 哈希表 字符串 滑动窗口
#  👍 48 👎 0

# 1二分
import collections


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        prefix = [(0, 0, 0)]
        for ch in s:
            a, b, c = prefix[-1]
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
            prefix.append((a, b, c))
        prefix = prefix[1:]

        def search(l, r, target, ch):
            while l < r:
                mid = (l + r) // 2
                if prefix[mid][ord(ch) - 97] < target:
                    l = mid + 1
                else:
                    r = mid
            return l

        n = len(prefix)
        ans = 0
        for i, (a, b, c) in enumerate(prefix):
            ch = s[i]
            if ch == 'a':
                index = max(search(i, n, b + 1, 'b'), search(i, n, c + 1, 'c'))
            elif ch == 'b':
                index = max(search(i, n, a + 1, 'a'), search(i, n, c + 1, 'c'))
            else:
                index = max(search(i, n, a + 1, 'a'), search(i, n, b + 1, 'b'))
            ans += n - index
        return ans


# 2双指针
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r = 0, 0
        m = collections.defaultdict(int)
        n = len(s)
        num = 0
        ans = 0
        while l <= n-3:
            while r < n and num != 7:
                num |= 1 << (ord(s[r]) - 97)
                m[s[r]] += 1
                r += 1
            if num==7:
                ans += n - r+1
            m[s[l]] -= 1
            if m[s[l]] == 0:
                num ^= 1 << (ord(s[l]) - 97)
            l+=1
        return ans

Solution().numberOfSubstrings("aaacb")
