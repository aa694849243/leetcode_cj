# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一些区域列表 regions ，每个列表的第一个区域都包含这个列表内所有其他区域。
#
#  很自然地，如果区域 X 包含区域 Y ，那么区域 X 比区域 Y 大。
#
#  给定两个区域 region1 和 region2 ，找到同时包含这两个区域的 最小 区域。
#
#  如果区域列表中 r1 包含 r2 和 r3 ，那么数据保证 r2 不会包含 r3 。
#
#  数据同样保证最小公共区域一定存在。
#
#
#
#  示例 1：
#
#
# 输入：
# regions = [["Earth","North America","South America"],
# ["North America","United States","Canada"],
# ["United States","New York","Boston"],
# ["Canada","Ontario","Quebec"],
# ["South America","Brazil"]],
# region1 = "Quebec",
# region2 = "New York"
# 输出："North America"
#
#
#
#
#  提示：
#
#
#  2 <= regions.length <= 10^4
#  region1 != region2
#  所有字符串只包含英文字母和空格，且最多只有 20 个字母。
#
#  Related Topics 树 深度优先搜索 广度优先搜索 数组 哈希表 字符串 👍 35 👎 0

# LCA 最短公共祖先
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        r1, r2 = region1, region2
        par = {}
        for li in regions:
            parent = li[0]
            for child in li[1:]:
                par[child] = parent
        r1set = set()
        while r1 in par:
            r1set.add(r1)
            r1 = par[r1]
        while r2 in par:
            if r2 in r1set:
                return r2
            r2 = par[r2]
        return r2  # 最后返回r2因为可能r1指到头，那时r1不包含在r1set里


Solution().findSmallestRegion(
    [["Earth", "North America", "South America"], ["North America", "United States", "Canada"],
     ["United States", "New York", "Boston"], ["Canada", "Ontario", "Quebec"], ["South America", "Brazil"]], "Canada",
    "South America")
