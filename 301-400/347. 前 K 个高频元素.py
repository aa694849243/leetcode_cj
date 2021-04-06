'''给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

 

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

from collections import Counter


# sort函数key参数
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        b = sorted(a.items, key=lambda x: x[1], reverse=True)
        ans = [b[i][0] for i in range(k)]
        return ans


# Counter用法
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]


# 堆
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        if not k:
            return []
        a = Counter(nums)
        b = list(a.keys())

        def sifdown(lst, e, begin, end):
            i, j = begin, 2 * begin + 1
            while j < end:
                if j + 1 < end and a[lst[j + 1]] < a[lst[j]]:
                    j += 1
                if a[e] < a[lst[j]]:
                    break
                lst[i] = lst[j]
                i, j = j, j * 2 + 1
            lst[i] = e

        def heap_build(lst):
            l = len(lst) // 2
            for i in range(l, -1, -1):
                sifdown(lst, lst[i], i, len(lst))

        c = b[:k]
        heap_build(c)
        for i in range(k, len(b)):
            if a[c[0]] < a[b[i]]:
                c[0] = b[i]
                sifdown(c, c[0], 0, k)
        return c


# 快速排序
class Solution:
    def topKFrequent(self, nums, k):
        if not k:
            return []
        a = Counter(nums)
        b = list(a.keys())

        def quick_sort(lst, begin, end,lth):
            e = lst[begin]
            i = begin
            for j in range(begin + 1, end + 1):
                if a[lst[j]] > a[e]:
                    i += 1
                    lst[i], lst[j] = lst[j], lst[i]
            lst[begin], lst[i] = lst[i], lst[begin]
            if i-begin+1==lth:
                return lst[:i+1]
            elif i-begin+1<lth:
                return quick_sort(lst, i + 1, end,lth-(i-begin+1))
            else:
                return quick_sort(lst,begin,i-1,lth)

        return quick_sort(b, 0, len(b) - 1,k)


nums = [1,1,1,2,2,2,3,3,3];
k = 3
Solution().topKFrequent(nums, k)
