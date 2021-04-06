'''给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组（的长度）。

 

示例 1:

输入: [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
 

注意: 给定的二进制数组的长度不会超过50000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contiguous-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

# 1巧妙的解法
# https://leetcode-cn.com/problems/contiguous-array/msolution/lian-xu-shu-zu-by-leetcode/
import collections


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m = {0: -1}
        cnt = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt -= 1
            else:
                cnt += 1
            if cnt not in m:
                m[cnt] = i
            else:
                ans = max(ans, i - m[cnt])
        return ans
