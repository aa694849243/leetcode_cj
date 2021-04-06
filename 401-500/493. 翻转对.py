'''给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3
注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1归并 超时
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(l, r):
            if r - l <= 1:
                return 0
            mid = (l + r) // 2
            cnt = 0
            cnt += merge(l, mid)
            cnt += merge(mid, r)
            i = l
            while i < mid:
                lo, hi = mid, mid
                while lo < r and nums[i] <= 2 * nums[lo]:
                    lo += 1
                while hi < r and nums[i] > 2 * nums[hi]:
                    hi += 1
                cnt += hi - lo if hi - lo > 0 else 0
                i += 1
            merge_sort(l, mid, r)
            return cnt

        def merge_sort(l, mid, r):
            x = []
            i, j = l, mid
            while i < mid and j < r:
                if nums[i] < nums[j]:
                    x.append(nums[i])
                    i += 1
                else:
                    x.append(nums[j])
                    j += 1
            if i < mid:
                x.extend(nums[i:mid])
            if j < r:
                x.extend(nums[j:r])
            nums[l:r] = x[:]

        return merge(0, len(nums))


# 1归并 逆序改良
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(l, r):
            if r - l <= 1:
                return 0
            mid = (l + r) // 2
            cnt = 0
            cnt += merge(l, mid)
            cnt += merge(mid, r)
            i = l
            p = mid
            while i < mid:
                while p < r and nums[i] <= 2 * nums[p]:
                    p += 1
                cnt += r - p
                i += 1
            merge_sort(l, mid, r)
            return cnt

        def merge_sort(l, mid, r):  # 逆序
            x = []
            i, j = l, mid
            while i < mid and j < r:
                if nums[i] > nums[j]:
                    x.append(nums[i])
                    i += 1
                else:
                    x.append(nums[j])
                    j += 1
            if i < mid:
                x.extend(nums[i:mid])
            if j < r:
                x.extend(nums[j:r])
            nums[l:r] = x[:]

        return merge(0, len(nums))


# 2树状数组
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def quiry(p, base):
            cnt = 0
            while p > 0:
                cnt += base[p]
                p -= p & -p
            return cnt

        def update(rank, base):
            while rank <= len(ranks):
                base[rank] += 1
                rank += rank & -rank

        ranks = {}
        rank = 1
        treeval = nums.copy()
        for num in nums:
            treeval.append(num / 2)
        treeval.sort()
        for num in treeval:
            if num not in ranks:
                ranks[num] = rank
                rank += 1
        base = [0] * (len(ranks) + 1)
        cnt = 0
        for i in range(len(nums) - 1, -1, -1):
            cnt += quiry(ranks[nums[i] / 2]-1, base)
            update(ranks[nums[i]], base)
        return cnt


Solution().reversePairs([1, 3, 2, 3, 1])

