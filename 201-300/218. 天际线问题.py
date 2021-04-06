'''
城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。现在，假设您获得了城市风光照片（图A）上显示的所有建筑物的位置和高度，请编写一个程序以输出由这些建筑物形成的天际线（图B）。



每个建筑物的几何信息用三元组 [Li，Ri，Hi] 表示，其中 Li 和 Ri 分别是第 i 座建筑物左右边缘的 x 坐标，Hi 是其高度。可以保证 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX 和 Ri - Li > 0。您可以假设所有建筑物都是在绝对平坦且高度为 0 的表面上的完美矩形。

例如，图A中所有建筑物的尺寸记录为：[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 。

输出是以 [ [x1,y1], [x2, y2], [x3, y3], ... ] 格式的“关键点”（图B中的红点）的列表，它们唯一地定义了天际线。关键点是水平线段的左端点。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，并始终为零高度。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

例如，图B中的天际线应该表示为：[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]。

说明:

任何输入列表中的建筑物数量保证在 [0, 10000] 范围内。
输入列表已经按左 x 坐标 Li  进行升序排列。
输出列表必须按 x 位排序。
输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-skyline-problem
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def merge_pass(buildings):
            if not buildings or not buildings[0]:
                return []
            n = len(buildings)
            if n == 1:
                return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
            else:
                return merge(merge_pass(buildings[:n // 2]), merge_pass(buildings[n // 2:]))

        def merge(left, right):
            ln, rn = len(left), len(right)
            left_y = right_y = cur_y = 0
            output = []
            l, r = 0, 0
            while l < ln and r < rn:
                pl = left[l]
                pr = right[r]
                if pl[0] < pr[0]:
                    x = pl[0]
                    left_y = pl[1]
                    l += 1
                else:
                    x = pr[0]
                    right_y = pr[1]
                    r += 1
                max_y = max(left_y, right_y)
                if cur_y != max_y:
                    if not output or output[-1][0] != x:
                        output.append([x, max_y])
                    else:
                        output[-1][1] = max_y
                    cur_y = max_y
            if l < ln:  # 合并的最后的端点一定是高度为0，如果存在重合，y轴一定取新的
                if output[-1][0] == left[l][0]:
                    output[-1][1] = left[l][1]
                    l += 1
                output.extend(left[l:])
            if r < rn:
                if output[-1][0] == right[r][0]:
                    output[-1][1] = right[r][1]
                    r += 1
                output.extend(right[r:])
            return output

        return merge_pass(buildings)


# class Solution:
#     def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
#         """
#         Divide-and-conquer algorithm to solve skyline problem,
#         which is similar with the merge sort algorithm.
#         """
#         n = len(buildings)
#         # The base cases
#         if n == 0:
#             return []
#         if n == 1:
#             x_start, x_end, y = buildings[0]
#             return [[x_start, y], [x_end, 0]]
#
#             # If there is more than one building,
#         # recursively divide the input into two subproblems.
#         left_skyline = self.getSkyline(buildings[: n // 2])
#         right_skyline = self.getSkyline(buildings[n // 2:])
#
#         # Merge the results of subproblem together.
#         return self.merge_skylines(left_skyline, right_skyline)
#
#     def merge_skylines(self, left, right):
#         """
#         Merge two skylines together.
#         """
#
#         def update_output(x, y):
#             """
#             Update the final output with the new element.
#             """
#             # if skyline change is not vertical -
#             # add the new point
#             if not output or output[-1][0] != x:
#                 output.append([x, y])
#             # if skyline change is vertical -
#             # update the last point
#             else:
#                 output[-1][1] = y
#
#         def append_skyline(p, lst, n, y, curr_y):
#             """
#             Append the rest of the skyline elements with indice (p, n)
#             to the final output.
#             """
#             while p < n:
#                 x, y = lst[p]
#                 p += 1
#                 if curr_y != y:
#                     update_output(x, y)
#                     curr_y = y
#
#         n_l, n_r = len(left), len(right)
#         p_l = p_r = 0
#         curr_y = left_y = right_y = 0
#         output = []
#
#         # while we're in the region where both skylines are present
#         while p_l < n_l and p_r < n_r:
#             point_l, point_r = left[p_l], right[p_r]
#             # pick up the smallest x
#             if point_l[0] < point_r[0]:
#                 x, left_y = point_l
#                 p_l += 1
#             else:
#                 x, right_y = point_r
#                 p_r += 1
#             # max height (i.e. y) between both skylines
#             max_y = max(left_y, right_y)
#             # if there is a skyline change
#             if curr_y != max_y:
#                 update_output(x, max_y)
#                 curr_y = max_y
#
#         # there is only left skyline
#         append_skyline(p_l, left, n_l, left_y, curr_y)
#
#         # there is only right skyline
#         append_skyline(p_r, right, n_r, right_y, curr_y)
#
#         return output


# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/the-skyline-problem/solution/tian-ji-xian-wen-ti-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
buildings = [[2, 4, 7], [2, 4, 5], [2, 4, 6]]
Solution().getSkyline(buildings)
