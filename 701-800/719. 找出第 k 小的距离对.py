'''给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。

示例 1:

输入：
nums = [1,3,1]
k = 1
输出：0
解释：
所有数对如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
提示:

2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import heapq


# 1堆 超时
class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        heap = [(nums[i + 1] - nums[i], i, i + 1)
                for i in range(len(nums) - 1)]
        heapq.heapify(heap)

        for _ in range(k):
            d, root, nei = heapq.heappop(heap)
            if nei + 1 < len(nums):
                heapq.heappush((nums[nei + 1] - nums[root], root, nei + 1))
        return d


# 2二分
import collections


class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        w = nums[-1]
        prefix = [0] * (w + 1)  # 前缀和i处表示nums中小于等于i的数量，比如nums=[1,1,1,5];prefix=[0,3,3,3,3,4],因为1有3个所以prefix[1]=3,1<2<3<4,所以prefix[2][3][4]均为3
        count = collections.Counter(nums)

        def bis_cal(num):  # 算距离小于num的数对数量
            return sum(prefix[min(nums[i] + num, w)] - prefix[nums[i]] + count[nums[i]] - multiplicity[i] for i in range(len(
                nums)))  # 公式中multiplicty[i]原始为count[nums[i]]-mul[i]，最终合起来与multiplicity[i]累加是相等的，比如[1,1,1,5] 的mul为[1,2,3],multi为[0,1,2],count为[3,3,3]

        left = 0
        for i in range(len(prefix)):
            while left < len(nums) and nums[left] == i:
                left += 1
            prefix[i] = left
        multiplicity = [0] * len(nums)  # mul表示nums中在i处之前等于nums[i]数的数量，比如nums=[1,1,1,2];mul=[0,1,2,0]
        a = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                a += 1
            else:
                a = 0
            multiplicity[i] = a
        l, r = 0, nums[-1] - nums[0] + 1
        while l < r:
            mid = (l + r) // 2
            if bis_cal(mid) < k:
                l = mid + 1
            else:
                r = mid

        return l


# 3双指针+二分
class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()

        def bis_cal(size):
            left = 0
            right = 0
            count = 0
            while right < len(nums):
                while nums[right] - nums[left] > size:
                    left += 1
                count += right - left
                right += 1
            return count

        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            if bis_cal(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l


Solution().smallestDistancePair([1, 6, 1], 3)
