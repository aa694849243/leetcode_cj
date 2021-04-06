'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

#------------------------caojie-96%--------双指针-------------------------------------------‘
#题解---https://leetcode-cn.com/problems/trapping-rain-water/solution/shuang-zhi-zhen-fa-by-aa694849243/
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 1, len(height) - 2
        area = 0
        leftsum = 0
        rightsum = 0
        leftmax = 0
        rightmax = len(height) - 1
        if len(height) == 1:
            return 0
        # while left < right:
        #     if height[left] != 0:
        #         break
        #     left += 1
        #     leftmax += 1
        # while right >= 0:
        #     if height[right] != 0:
        #         break
        #     right -= 1
        #     rightmax -= 1
        while leftmax < rightmax:
            if height[leftmax] <= height[rightmax]:
                if height[left] >= height[leftmax]:
                    area = area + (left - leftmax - 1) * height[leftmax] - leftsum
                    leftmax = left
                    leftsum = 0
                else:
                    leftsum += height[left]
                left += 1
            else:
                if height[right] >= height[rightmax]:
                    area = area + (rightmax - right - 1) * height[rightmax] - rightsum
                    rightmax = right
                    rightsum = 0
                else:
                    rightsum += height[right]
                right -= 1
        return area


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [2, 0, 2]
Solution().trap(height)
