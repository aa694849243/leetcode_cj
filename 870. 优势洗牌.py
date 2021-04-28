# 给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。 
# 
#  返回 A 的任意排列，使其相对于 B 的优势最大化。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [2,7,11,15], B = [1,10,4,11]
# 输出：[2,11,7,15]
#  
# 
#  示例 2： 
# 
#  输入：A = [12,24,8,32], B = [13,25,32,11]
# 输出：[24,32,8,12]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length = B.length <= 10000 
#  0 <= A[i] <= 10^9 
#  0 <= B[i] <= 10^9 
#  
#  Related Topics 贪心算法 数组
#  👍 122 👎 0

from typing import List
# 田忌赛马
import heapq
import collections


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        a, b = A.copy(), B.copy()
        heapq.heapify(a)
        heapq.heapify(b)
        remain = []
        assign = collections.defaultdict(list)
        while a:
            if a[0] > b[0]:
                assign[heapq.heappop(b)].append(heapq.heappop(a))
            else:
                remain.append(heapq.heappop(a))
        ans = []
        for x in B:
            if assign[x]:
                ans.append(assign[x].pop())
            else:
                ans.append(remain.pop())
        return ans
