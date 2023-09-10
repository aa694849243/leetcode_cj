# 中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
#
#  例如：
#
#
#  [2,3,4]，中位数是 3
#  [2,3]，中位数是 (2 + 3) / 2 = 2.5
#
#
#  给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗
# 口中元素的中位数，并输出由它们组成的数组。
#
#
#
#  示例：
#
#  给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。
#
#
# 窗口位置                      中位数
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7      -1
#  1  3 [-1  -3  5] 3  6  7      -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
#
#
#  因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。
#
#
#
#  提示：
#
#
#  你可以假设 k 始终有效，即：k 始终小于等于输入的非空数组的元素个数。
#  与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
#
#
#  Related Topics 数组 哈希表 滑动窗口 堆（优先队列）
#  👍 427 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import heapq


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left, right = [], []
        for i, num in enumerate(nums[:k]):
            heapq.heappush(left, (-num, -i))
        for i in range(k // 2):
            heapq.heappush(right, (-left[0][0], -left[0][1]))
            heapq.heappop(left)
        ans = [-left[0][0] if k % 2 else (right[0][0] - left[0][0]) / 2]
        left_num, right_num = len(left), len(right)
        for i in range(k, len(nums)):
            heapq.heappush(left, (-nums[i], -i))
            heapq.heappush(right, (-left[0][0], -left[0][1]))
            heapq.heappop(left)
            heapq.heappush(left, (-right[0][0], -right[0][1]))
            heapq.heappop(right)
            left_num += 1
            pop_ = -nums[i - k], -(i - k)
            if pop_ == left[0]:
                left_num -= 1
                heapq.heappop(left)
            elif pop_ < left[0]:  # 弹出值在右边
                right_num -= 1
            else:
                left_num -= 1
            if k % 2:
                while left_num - 1 > right_num:
                    num, idx = heapq.heappop(left)
                    num, idx = -num, -idx
                    if idx <= i - k:
                        continue
                    heapq.heappush(right, (num, idx))
                    left_num -= 1
                    right_num += 1
                while left_num - 1 < right_num:
                    num, idx = heapq.heappop(right)
                    if idx <= i - k:
                        continue
                    heapq.heappush(left, (-num, -idx))
                    left_num += 1
                    right_num -= 1
            else:
                while left_num > right_num:
                    num, idx = heapq.heappop(left)
                    num, idx = -num, -idx
                    if idx <= i - k:
                        continue
                    heapq.heappush(right, (num, idx))
                    left_num -= 1
                    right_num += 1
                while left_num < right_num:
                    num, idx = heapq.heappop(right)
                    if idx <= i - k:
                        continue
                    heapq.heappush(left, (-num, -idx))
                    left_num += 1
                    right_num -= 1
            while left and -left[0][1] <= i - k:
                heapq.heappop(left)
            while right and right[0][1] <= i - k:
                heapq.heappop(right)
            ans.append(-left[0][0] if k % 2 else (right[0][0] - left[0][0]) / 2)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().medianSlidingWindow(
    [1, 2, 3, 4, 2, 3, 1, 4, 2],
    3
))
