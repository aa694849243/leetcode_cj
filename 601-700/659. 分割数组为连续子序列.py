'''给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个长度至少为 3 的子序列，其中每个子序列都由连续整数组成。

如果可以完成上述分割，则返回 true ；否则，返回 false 。

 

示例 1：

输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3
3, 4, 5
示例 2：

输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3, 4, 5
3, 4, 5
示例 3：

输入: [1,2,3,4,4,5]
输出: False
 

提示：

1 <= nums.length <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

# 1堆+哈希
import heapq
import collections


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        m = collections.defaultdict(list)
        for i in range(len(nums)):
            if not m[nums[i] - 1]:
                heapq.heappush(m[nums[i]], 1)
            else:
                a = heapq.heappop(m[nums[i] - 1])
                heapq.heappush(m[nums[i]], a + 1)
        for i in m:
            if m[i] and m[i][0] < 3:
                return False
        return True


# 2哈希+贪心
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)
        m = collections.defaultdict(int)
        for i in range(len(nums)):
            if m[nums[i] - 1] > 0:
                m[nums[i] - 1] -= 1
                m[nums[i]] += 1
            else:
                if c[nums[i] + 1] <= 0 or c[nums[i] + 2] <= 0:
                    return False
                m[nums[i]] += 1
                c[nums[i] + 1] -= 1
                c[nums[i] + 2] -= 1
            c[nums[i]] -= 1
        return True


Solution().isPossible([3, 4, 4, 5, 6, 7])
