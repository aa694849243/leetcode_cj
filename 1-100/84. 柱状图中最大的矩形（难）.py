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

#此方法为改良版的哨兵+单调栈，改良方法参考网站，特别注意关于右边界的问题
# https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        left, right = [], [len(heights) for _ in range(len(heights))]
        stack = []
        i = 0
        while i < len(heights):
            while stack and heights[stack[-1]] >= heights[i]:
                j = stack.pop()
                right[j] = i
            if not stack:
                left.append(-1)
            else:
                left.append(stack[-1])
            stack.append(i)
            i+=1
        maxarea=max([(right[i]-left[i]-1)*heights[i] for i in range(len(heights))])
        return maxarea


Solution().largestRectangleArea([4,0,0,3,0])
