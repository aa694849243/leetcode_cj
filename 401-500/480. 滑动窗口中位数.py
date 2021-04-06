'''中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

例如：

[2,3,4]，中位数是 3
[2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

 

示例：

给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。

窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。

 

提示：

你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-median
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

# 两个堆中位数 延迟删除 延迟更新
import heapq
import collections


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums
        m = collections.defaultdict(int) #需要延迟删除数字的字典
        if k % 2:
            l = k // 2
            r = k // 2 + 1
            diff = 1
        else:
            l = r = k // 2
            diff = 0
        lmi = []
        rma = []
        for i in range(k):
            heapq.heappush(rma, nums[i])  # 小顶堆存右半边
        for i in range(k // 2):
            heapq.heappush(lmi, -heapq.heappop(rma))  # 大顶堆存左半边
        ans = [rma[0] if r > l else (rma[0] - lmi[0]) / 2]
        for i in range(k, len(nums)):
            m[nums[i - k]] += 1
            l += 1  # 每次都加一个数加到右半组，再从右半组弹一个数到左半组，相当于给左半组加了1个
            if nums[i - k] <= -lmi[0]:
                l -= 1
            else:
                r -= 1
            heapq.heappush(lmi, -heapq.heappushpop(rma, nums[i]))
            if r - l > diff:  # 右半边比较多
                heapq.heappush(lmi, -heapq.heappop(rma))
                l += 1
            elif r - l < diff:
                heapq.heappush(rma, -heapq.heappop(lmi))
                r += 1
                l -= 1
            while m[-lmi[0]] > 0:
                num = -heapq.heappop(lmi)
                m[num] -= 1
            while m[rma[0]] > 0:
                num = heapq.heappop(rma)
                m[num] -= 1
            ans.append(rma[0] if r > l else (rma[0] - lmi[0]) / 2)
        return ans


Solution().medianSlidingWindow([1, 1, 1, 1], 2)
