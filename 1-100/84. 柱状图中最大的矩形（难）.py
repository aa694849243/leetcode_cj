'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 



以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

 



图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# 此方法为改良版的哨兵+单调栈，改良方法参考网站，特别注意关于右边界的问题
# https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
# 延迟单调栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        left, right = [-1] * n, [n] * n
        for i,h in enumerate(heights):
            while stk and heights[stk[-1]] >= h:
                right[stk.pop()] = i
            left[i] = stk[-1] if stk else -1
            stk.append(i)
        return max((right[i] - left[i] - 1) * heights[i] for i in range(n))



Solution().largestRectangleArea([4, 0, 0, 3, 0])
