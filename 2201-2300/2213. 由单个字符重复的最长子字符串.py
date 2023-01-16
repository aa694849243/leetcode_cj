# -*- coding: utf-8 -*-
# 给你一个下标从 0 开始的字符串 s 。另给你一个下标从 0 开始、长度为 k 的字符串 queryCharacters ，一个下标从 0 开始、长度也是
# k 的整数 下标 数组 queryIndices ，这两个都用来描述 k 个查询。
#
#  第 i 个查询会将 s 中位于下标 queryIndices[i] 的字符更新为 queryCharacters[i] 。
#
#  返回一个长度为 k 的数组 lengths ，其中 lengths[i] 是在执行第 i 个查询 之后 s 中仅由 单个字符重复 组成的 最长子字符串 的
#  长度 。
#
#
#
#  示例 1：
#
#
# 输入：s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
# 输出：[3,3,4]
# 解释：
# - 第 1 次查询更新后 s = "bbbacc" 。由单个字符重复组成的最长子字符串是 "bbb" ，长度为 3 。
# - 第 2 次查询更新后 s = "bbbccc" 。由单个字符重复组成的最长子字符串是 "bbb" 或 "ccc"，长度为 3 。
# - 第 3 次查询更新后 s = "bbbbcc" 。由单个字符重复组成的最长子字符串是 "bbbb" ，长度为 4 。
# 因此，返回 [3,3,4] 。
#
#  示例 2：
#
#
# 输入：s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
# 输出：[2,3]
# 解释：
# - 第 1 次查询更新后 s = "abazz" 。由单个字符重复组成的最长子字符串是 "zz" ，长度为 2 。
# - 第 2 次查询更新后 s = "aaazz" 。由单个字符重复组成的最长子字符串是 "aaa" ，长度为 3 。
# 因此，返回 [2,3] 。
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 10⁵
#  s 由小写英文字母组成
#  k == queryCharacters.length == queryIndices.length
#  1 <= k <= 10⁵
#  queryCharacters 由小写英文字母组成
#  0 <= queryIndices[i] < s.length
#
#
#  Related Topics 线段树 数组 字符串 有序集合
#  👍 28 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import itertools
from typing import List
from sortedcontainers import SortedList, SortedDict


# 珂朵莉树
# https://leetcode.cn/problems/longest-substring-of-one-repeating-character/solution/python-guo-ran-wo-huan-shi-geng-xi-huan-olhop/
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        def split(idx):  # 切割，idx为第二段起点
            if idx < 0 or idx >= n:
                return
            cur = s_map.bisect_right(idx) - 1
            st, end = s_map.peekitem(cur)
            if idx == st:  # 如果idx本身就是起点，则直接返回，留到idx+1处理
                return
            s_map[st] = idx - 1
            s_map[idx] = end
            s_list.remove(end - st + 1)
            s_list.add(idx - st)
            s_list.add(end - idx + 1)

        def union(idx):  # 合并，idx向左合并
            if idx < 0 or idx >= n:
                return
            cur = s_map.bisect_right(idx) - 1
            pre = cur - 1
            if pre < 0:  # 最左端，无法向左合并
                return
            (s1, e1), (s2, e2) = s_map.peekitem(pre), s_map.peekitem(cur)
            if chars[s1] == chars[s2]:
                s_map[s1] = e2
                s_map.pop(s2)
                s_list.remove(e1 - s1 + 1)
                s_list.remove(e2 - s2 + 1)
                s_list.add(e2 - s1 + 1)

        n = len(s)
        chars = list(s)
        s_map = SortedDict()
        s_list = SortedList()
        start = 0
        for _, group in itertools.groupby(s):
            s_map[start] = start + (length := len(list(group))) - 1
            s_list.add(length)
            start += length
        res = [1] * len(queryIndices)
        for i, (c, idx) in enumerate(zip(queryCharacters, queryIndices)):
            if chars[idx] == c:
                res[i] = s_list[-1]
                continue
            chars[idx] = c
            split(idx)
            split(idx + 1)
            union(idx)
            union(idx + 1)
            res[i] = s_list[-1]
        return res

# 列表线段树 合并前后缀
# https://leetcode.cn/problems/longest-substring-of-one-repeating-character/solution/by-endlesscheng-qpbw/
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        pre = [1] * (4 * n)
        suf = [1] * (4 * n)
        tree = [1] * (4 * n)

        def maintain(o, l, r):  # o为从1开始的节点
            pre[o] = pre[o << 1]
            suf[o] = suf[o << 1 | 1]
            tree[o] = max(tree[o << 1], tree[o << 1 | 1])
            mid = (l + r) >> 1  # mid-1为s中的正中间
            if chars[mid] == chars[mid - 1]:  # 合并 mid-1为左子树的最右端，mid为右子树的最左端
                if suf[o << 1] == mid - l + 1:  # 左子树后缀长度等于左子树长度
                    pre[o] += pre[o << 1 | 1]  # 前缀合并到父节点
                if pre[o << 1 | 1] == r - mid:  # 右子树前缀长度等于右子树长度
                    suf[o] += suf[o << 1]  # 后缀合并到父节点
                tree[o] = max(tree[o], suf[o << 1] + pre[o << 1 | 1])  # 更新最大长度

        def build(o, l, r):
            if l == r:
                tree[o] = pre[o] = suf[o] = 1
                return
            mid = (l + r) >> 1
            build(o << 1, l, mid)
            build(o << 1 | 1, mid + 1, r)
            maintain(o, l, r)

        def update(o, l, r, idx):
            if l == r:
                return
            mid = (l + r) >> 1
            if idx <= mid:
                update(o << 1, l, mid, idx)
            else:
                update(o << 1 | 1, mid + 1, r, idx)
            maintain(o, l, r)

        chars=list(s)
        build(1, 1, n)
        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            if chars[idx] != ch:
                chars[idx] = ch
                update(1, 1, n, idx + 1)
            res.append(tree[1])
        return res


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().longestRepeating(s="bbbbbbbbacc", queryCharacters="cb", queryIndices=[3, 3]))
