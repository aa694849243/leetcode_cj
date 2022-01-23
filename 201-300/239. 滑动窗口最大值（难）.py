'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

进阶：

你能在线性时间复杂度内解决此题吗？

 

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import deque
from typing import List


# 双端队列 滑动窗口
# 递减队列，队首保留坐标
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            if que and que[0] == i - k:
                que.popleft()
            while que and nums[i] >= nums[que[-1]]:
                que.pop()
            que.append(i)

        que = deque()
        ans = []
        for i in range(k):
            clean_deque(i)
        max_nums = nums[que[0]]
        ans.append(max_nums)
        for i in range(k, len(nums)):
            clean_deque(i)
            ans.append(nums[que[0]])
        return ans


# 动态规划 双层遍历
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        len1 = len(nums)
        left = [0] * len1
        right = [0] * len1
        i = 0
        while i < len1:
            max_ = float('-inf')
            for j in range(k):
                max_ = max(max_, nums[i])
                left[i] = max_
                i += 1
                if i >= len1:
                    break
        n = len1 % k
        max_ = float('-inf')
        for i in range(len1 - 1, len1 - 1 - n, -1):
            max_ = max(nums[i], max_)
            right[i] = max_
        i -= 1
        while i >= 0:
            max_ = float('-inf')
            for j in range(k):
                max_ = max(max_, nums[i])
                right[i] = max_
                i -= 1
        ans = []
        for i in range(k - 1, len1):
            ans.append(max(left[i], right[i - k + 1]))
        return ans


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))

        return output


# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetcode-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
