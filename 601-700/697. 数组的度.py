'''给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

 

示例 1：

输入：[1, 2, 2, 3, 1]
输出：2
解释：
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2：

输入：[1,2,2,3,1,4,2]
输出：6
 

提示：

nums.length 在1到 50,000 区间范围内。
nums[i] 是一个在 0 到 49,999 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/degree-of-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        a = collections.Counter(nums)
        flag = max(a.values())
        for key in list(a.keys()):
            if a[key] != flag:
                a.pop(key)
        q = collections.deque()
        ans = float('inf')
        x = 0
        for i in range(len(nums)):
            q.append(nums[i])
            if nums[i] in a:
                a[nums[i]] -= 1
                if a[nums[i]] == 0:
                    while q[0] != nums[i]:
                        if q[0] in a:
                            a[q[0]] += 1
                        q.popleft()
                    ans = min(ans, len(q))

        return ans

#海象表达式
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp = dict()

        for i, num in enumerate(nums):
            if num in mp:
                mp[num][0] += 1
                mp[num][2] = i
            else:
                mp[num] = [1, i, i]

        maxNum = minLen = 0
        for count, left, right in mp.values():
            if maxNum < count:
                maxNum = count
                minLen = right - left + 1
            elif maxNum == count:
                if minLen > (span := right - left + 1):
                    minLen = span

        return minLen


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / degree - of - an - array / solution / shu - zu - de - du - by - leetcode - solution - ig97 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
Solution().findShortestSubArray([1,1,2,1,3,3,3,1,3,1,3])
