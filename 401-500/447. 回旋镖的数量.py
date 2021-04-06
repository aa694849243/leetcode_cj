'''给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

返回平面上所有回旋镖的数量。

 
示例 1：

输入：points = [[0,0],[1,0],[2,0]]
输出：2
解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
示例 2：

输入：points = [[1,1],[2,2],[3,3]]
输出：2
示例 3：

输入：points = [[1,1]]
输出：0
 

提示：

n == points.length
1 <= n <= 500
points[i].length == 2
-104 <= xi, yi <= 104
所有点都 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-boomerangs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

import collections


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0
        memo = [collections.defaultdict(int) for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                a = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                memo[i][a] += 1
                memo[j][a] += 1
        res = 0
        for i in range(len(memo)):
            for j in memo[i]:
                res += memo[i][j]*(memo[i][j]-1)
        return res
points = [[1,1],[2,2],[3,3]]
Solution().numberOfBoomerangs(points)
