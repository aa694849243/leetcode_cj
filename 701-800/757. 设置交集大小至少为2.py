'''一个整数区间 [a, b]  ( a < b ) 代表着从 a 到 b 的所有连续整数，包括 a 和 b。

给你一组整数区间intervals，请找到一个最小的集合 S，使得 S 里的元素与区间intervals中的每一个整数区间都至少有2个元素相交。

输出这个最小集合S的大小。

示例 1:

输入: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
输出: 3
解释:
考虑集合 S = {2, 3, 4}. S与intervals中的四个区间都有至少2个相交的元素。
且这是S最小的情况，故我们输出3。
示例 2:

输入: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
输出: 5
解释:
最小的集合S = {1, 2, 3, 4, 5}.
注意:

intervals 的长度范围为[1, 3000]。
intervals[i] 长度为 2，分别代表左、右边界。
intervals[i][j] 的值是 [0, 10^8]范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-intersection-size-at-least-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[
            1]))  # 假设两个区间[s,e],[s,e'],若e>e'，[s,e']应该更早考虑，因为[s,e]包含[s,e']，假如[s,s+1]在[s,e']中就一定在[s,e]中，所以先遍历到[s,e']的话[s,e]区间中的个数一定会减到0，相当于把[s,e]从区间中剔除了，不影响结果
        todo = [2] * len(intervals)
        ans = 0
        while intervals:
            n, (s, e) = todo.pop(), intervals.pop()
            for p in range(s, s + n):
                for i, (l, r) in enumerate(intervals):
                    if p <= r and todo[i] > 0:
                        todo[i] -= 1
                ans += 1
        return ans
