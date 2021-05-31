# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List


# 你想要用小写字母组成一个目标字符串 target。
#
#  开始的时候，序列由 target.length 个 '?' 记号组成。而你有一个小写字母印章 stamp。
#
#  在每个回合，你可以将印章放在序列上，并将序列中的每个字母替换为印章上的相应字母。你最多可以进行 10 * target.length 个回合。
#
#  举个例子，如果初始序列为 "?????"，而你的印章 stamp 是 "abc"，那么在第一回合，你可以得到 "abc??"、"?abc?"、"??abc
# "。（请注意，印章必须完全包含在序列的边界内才能盖下去。）
#
#  如果可以印出序列，那么返回一个数组，该数组由每个回合中被印下的最左边字母的索引组成。如果不能印出序列，就返回一个空数组。
#
#  例如，如果序列是 "ababc"，印章是 "abc"，那么我们就可以返回与操作 "?????" -> "abc??" -> "ababc" 相对应的答案
# [0, 2]；
#
#  另外，如果可以印出序列，那么需要保证可以在 10 * target.length 个回合内完成。任何超过此数字的答案将不被接受。
#
#
#
#  示例 1：
#
#  输入：stamp = "abc", target = "ababc"
# 输出：[0,2]
# （[1,0,2] 以及其他一些可能的结果也将作为答案被接受）
#
#
#  示例 2：
#
#  输入：stamp = "abca", target = "aabcaca"
# 输出：[3,0,1]
#
#
#
#
#  提示：
#
#
#  1 <= stamp.length <= target.length <= 1000
#  stamp 和 target 只包含小写字母。
#
#  Related Topics 贪心算法 字符串
#  👍 33 👎 0


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, N = len(stamp), len(target)
        base = [False] * N  # 终点情况
        q = collections.deque()
        st = []
        ans = []
        for i in range(N - n + 1):
            made, todo = set(), set()  # 以每个字符为起点，盖上戳后情况分析
            for j in range(n):
                if target[i + j] != stamp[j]:
                    todo.add(i + j)  # 不匹配的
                else:
                    made.add(i + j)  # 匹配的
            st.append((made, todo))
            if not todo:  # 完全匹配
                ans.append(i)  # 添加到答案
                for k in range(i, i + n):  # 将这一串添加到队列中，与这一串字符相交的部分进行下一步考察
                    if not base[k]:
                        q.append(k)
                        base[k] = True
        while q:
            j = q.popleft()
            for i in range(max(0, j - n + 1), min(j, N - n) + 1): #每个字母影响的窗口
                if j in st[i][1]:
                    st[i][1].discard(j) #被影响的窗口要剔掉，因为原来这个不匹配，因为后一个戳消除掉了，不匹配的这个字母可以为任意字母，也就匹配了
                    if not st[i][1]:
                        ans.append(i)
                        for k in st[i][0]:
                            if not base[k]:
                                base[k]=True
                                q.append(k)
        return ans[::-1] if all(base) else []
Solution().movesToStamp(stamp = "abca", target = "aabcaca")