'''给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。

定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。

找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。

示例 1:

输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
示例 2:

输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
示例 3:

输入: nums1 = [1,2], nums2 = [3], k = 3
输出: [1,3],[2,3]
解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
# 堆
import heapq
import itertools


# iteritools.product
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return map(list, heapq.nsmallest(k, itertools.product(nums1, nums2), key=sum))


# 解包 heapq.merge itertools.islice
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        streams = map(lambda u: ([u + v, u, v] for v in nums2), nums1)
        stream = heapq.merge(*streams)
        return [suv[1:] for suv in itertools.islice(stream, k)]


# 队列 特殊入队操作
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q = []

        def push(i, j):
            if i<len(nums1) and j<len(nums2):
                heapq.heappush(q, [nums1[i] + nums2[j], i, j])

        push(0, 0)
        ans = []
        while q and len(ans) < k:
            _, i, j = heapq.heappop(q)
            ans += [[nums1[i], nums2[j]]]
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return ans


a = [1, 2, 7, 10, 12]
b = [5, 6, 44, 66]
Solution().kSmallestPairs(a, b, 6)
