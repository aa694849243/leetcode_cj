'''
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc = Counter(t)
        dq = deque()
        res = ""
        mi = math.inf
        tmp = Counter()
        for i, ch in enumerate(s):
            if ch in tc:
                tmp[ch] += 1
                dq.append(i)
                while dq and tmp[s[dq[0]]] > tc[s[dq[0]]]:
                    tmp[s[dq.popleft()]] -= 1
                diff_c = tc - tmp
                if len(diff_c) <= 0 and i - dq[0] + 1 < mi:
                    mi = i - dq[0] + 1
                    res = s[dq[0]:i + 1]
        return res


#滑动窗口
#https://leetcode-cn.com/problems/minimum-window-substring/solution/zui-xiao-fu-gai-zi-chuan-by-leetcode-solution/
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        st = collections.Counter(t)
        ss = {}
        n = len(st)
        a = collections.deque()
        l, r = 0, 0
        distance = float('inf')
        ans = {}
        flag = 0
        while r < len(s):
            if s[r] in st:
                if not ss.get(s[r]):
                    ss[s[r]] = 1
                else:
                    ss[s[r]] += 1
                a.append(r)
                while ss[s[a[0]]]>st[s[a[0]]]:
                    ss[s[a[0]]] -=1
                    a.popleft()
                j = 0
                for i in st:
                    if ss.get(i) and st[i] <= ss[i]:
                        j += 1
                    else:
                        break
                if j == n:
                    flag = 1
                    l = a[0]
                    distance = min(r - l, distance)
                    if r - l == distance:
                        ans[distance] = l
            r += 1

        if not flag:
            return ''
        return s[ans[distance]:ans[distance] + distance + 1]


S = "ADOBECODEBANC"
T = "ABC"
Solution().minWindow(S, T)
