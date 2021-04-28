# 如果可以通过将 A 中的两个小写字母精确地交换位置 K 次得到与 B 相等的字符串，我们称字符串 A 和 B 的相似度为 K（K 为非负整数）。
#
#  给定两个字母异位词 A 和 B ，返回 A 和 B 的相似度 K 的最小值。
#
#
#
#  示例 1：
#
#  输入：A = "ab", B = "ba"
# 输出：1
#
#
#  示例 2：
#
#  输入：A = "abc", B = "bca"
# 输出：2
#
#
#  示例 3：
#
#  输入：A = "abac", B = "baca"
# 输出：2
#
#
#  示例 4：
#
#  输入：A = "aabc", B = "abca"
# 输出：2
#
#
#
#  提示：
#
#
#  1 <= A.length == B.length <= 20
#  A 和 B 只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母。
#
#  Related Topics 广度优先搜索 图
#  👍 95 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import itertools
import collections


# 1自环 截断 遍历全部可能性
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        a = [(a, b) for a, b in zip(s1, s2) if a != b]
        a = collections.Counter(a)
        alphabeta = 'abcdef'
        pairs = [(a, b) for a in alphabeta for b in alphabeta if a != b]
        index = {x: i for i, x in enumerate(pairs)}
        count = [0] * len(pairs)
        for x in a:  # 设置目标状态count
            count[index[x]] = a[x]
        seen = set()
        for size in range(2, 7):  # 遍历全部候选的状态
            for cand in itertools.permutations(alphabeta, size):
                i = cand.index(min(cand))  # 一个环是没有头的，所以我们把最小的字符设置为头
                cand = cand[i:] + cand[:i]
                seen.add(cand)
        possible = set()  # 将小环的状态数字化
        for cand in seen:
            status = [0] * len(pairs)
            for pair in zip(cand, cand[1:] + cand[:1]):
                status[index[pair]] += 1
            possible.add(tuple(status))
        inital = [0] * len(pairs)
        m = {tuple(inital): 0}

        def solve(status):
            if status in m: return m[status]
            ans = float('-inf')
            for cand in possible:
                status2 = list(status)
                for i, x in enumerate(cand):
                    if status2[i] < x:
                        break
                    else:
                        status2[i] -= x
                else:
                    ans = max(ans, 1 + solve(tuple(status2)))
            m[status] = ans
            return ans

        return sum(count) - solve(tuple(count))


# 2广度优先搜索
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def neighbor(s):
            for i in range(len(s1)):
                if s[i] != s2[i]:
                    break
            a = list(s)
            for j in range(i + 1, len(s)):
                if a[j] == s2[i]:
                    a[j], a[i] = a[i], a[j]
                    yield ''.join(a)
                    a[j], a[i] = a[i], a[j]

        q = collections.deque()
        q.append((s1, 0))
        seen={s1}
        while q:
            s, level = q.popleft()
            if s==s2: return level
            for nei in neighbor(s):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei,level+1))


Solution().kSimilarity("abac", "baca")
# leetcode submit region end(Prohibit modification and deletion)
