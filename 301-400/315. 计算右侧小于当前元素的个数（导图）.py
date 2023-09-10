from typing import List
import bisect


# 树状数组 fenwick树 lowbit函数 离散化
# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/chi-san-hua-shu-zhuang-shu-zu-pythonshi-xian-by-mi/
# 时间复杂度：我们梳理一下这个算法的流程，这里离散化使用哈希表去重，然后再对去重的数组进行排序，时间代价为 O(nlog n)；初始化树状数组的时间代价是O(n)；通过值获取离散化id 的操作单次时间代价为O(logn)；对于每个序列中的每个元素，都会做一次查询id、单点修改和前缀和查询，总的时间代价为O(nlogn)。故渐进时间复杂度为O(nlogn)。
# 空间复杂度：这里用到的离散化数组、树状数组、哈希表的空间代价都是O(n)，故渐进空间复杂度为 O(n)

class Solution:
    c = []
    l = 0

    def discretization(self, nums):
        a = sorted(list(set(nums)))
        return [bisect.bisect_left(a, num) + 1 for num in nums]  # 防止后序quiry函数溢出，从1开始

    def lowbit(self, num):
        return num & (-num)

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.c = [0] * (len(nums) + 2)
        self.l = len(nums)
        count = [0] * len(nums)
        buckets = self.discretization(nums)
        for i in range(len(nums) - 1, -1, -1):
            count[i] = self.quiry(buckets[i] - 1)
            self.update(buckets[i])
        return count

    def quiry(self, num):
        val = 0
        while num > 0:
            val += self.c[num]
            num -= self.lowbit(num)
        return val

    def update(self, num):
        while num <= self.l:
            self.c[num] += 1
            num += self.lowbit(num)

Solution().countSmaller([5,2,6,1])
# 投机取巧法
import bisect


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        sortns = []
        for i in range(len(nums) - 1, -1, -1):
            bisect.insort_left(sortns, nums[i])
            res.append(bisect.bisect_left(sortns, nums[i]))
        return res[::-1]


# 归并排序 归并法 求逆序数
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * n
        indexes = [i for i in range(n)]

        def mergesort(left, right):
            if right - left < 2:
                return
            mid = (left + right) // 2
            mergesort(left, mid)
            mergesort(mid, right)
            merge(left, mid, right)

        def merge(left, mid, right):
            pre = left;
            tmp = mid
            res = []
            while left < mid or tmp < right:
                if tmp == right or left < mid and nums[indexes[left]] <= nums[indexes[tmp]]:
                    res.append(indexes[left])
                    count[indexes[left]] += tmp - mid
                    left += 1
                else:
                    res.append(indexes[tmp])
                    tmp += 1
            indexes[pre:right] = res

        mergesort(0, n)
        return count


u = [5, 2, 6, 1]
Solution().countSmaller(u)
