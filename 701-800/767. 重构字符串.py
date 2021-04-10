'''给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""
注意:

S 只包含小写字母并且长度在[1, 500]区间内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorganize-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# 1堆
import collections
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        c = collections.Counter(S)
        length = len(S)
        if max(c.values()) > (length + 1) // 2:
            return ''
        a = []
        for ch in c:
            heapq.heappush(a, (-c[ch], ch))
        ans = []
        while len(a) > 1:
            x1, s1 = heapq.heappop(a)
            x2, s2 = heapq.heappop(a)
            ans.extend([s1, s2])
            c[s1] -= 1
            c[s2] -= 1
            if c[s1] > 0:
                heapq.heappush(a, (-c[s1], s1))
            if c[s2] > 0:
                heapq.heappush(a, (-c[s2], s2))
        if a:
            ans.append(a[0][1])
        return ''.join(ans)


# 2贪心 奇偶排列
class Solution:
    def reorganizeString(self, S: str) -> str:
        c = collections.Counter(S)
        length = len(S)
        if max(c.values()) > (length + 1) // 2:
            return ''
        odd, even = 1, 0  # 奇偶指针
        half = length // 2+1
        ans = [''] * length
        for ch, cnt in c.items():
            while cnt > 0 and cnt < half and odd <= length - 1:
                ans[odd] = ch
                cnt -= 1
                odd += 2
            while cnt > 0:
                ans[even] = ch
                cnt -= 1
                even += 2
        return ''.join(ans)


Solution().reorganizeString("abb")
