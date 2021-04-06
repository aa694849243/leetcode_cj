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
        ls, lt = len(s), len(t)

        mem = {}
        for i in range(ls):
            if s[i] in t:
                if not mem.get(s[i]):
                    mem[s[i]] = [i]
                else:
                    mem[s[i]].append(i)
        if not mem:
            return ''
        product = [[]]
        for k in range(lt):
            # if k - 1>=0 and t[k - 1] == t[k]:
            #     continue
            if not mem.get(t[k]):
                return ''
            x = []
            for i in product:
                for j in mem[t[k]]:
                    if j not in i:
                        x.append(i + [j])
            product = x
            # product = [i + [j] for i in product for j in mem[t[k]] if j not in i]
        if not product[0] or len(product[0]) < lt:
            return ''
        M = float('inf')
        for i in product:
            M = min(M, max(i) - min(i))
            if max(i) - min(i) == M:
                ans = s[min(i):max(i) + 1]
        return ans


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
