'''
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-gap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        d = len(str(max(nums)))
        llen = len(nums)
        rlist = [[] for _ in range(10)]
        for m in range(d):
            for j in range(llen):
                rlist[int(str(nums[j] // (10 ** m))[-1])].append(nums[j])
            j = 0
            for r in range(10):
                tmp = rlist[r]
                for k in range(len(tmp)):
                    nums[j] = tmp[k]
                    j += 1
                rlist[r].clear()
        maxdiff = 0
        for i in range(1, llen):
            maxdiff = max(maxdiff, nums[i] - nums[i - 1])
        return maxdiff


# 数学 桶排序 基数排序
# 为什么最大间距不会出现在桶内
# 如果数组里的数是均匀分布的，那么最大间距就是桶的大小。 如果不是均匀分布，最大间距一定大于桶的大小，所以最大间距不会出现在桶内。 如果是均匀分布的，任意两个数字之间的间距就是最大间距，也可以通过相邻桶计算出来
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums) < 2:
            return 0
        bucket = (max(nums) - min(nums)) // (len(nums) - 1)
        m = min(nums)
        bucket_num = (max(nums) - m) // bucket + 1
        s = [[] for _ in range(bucket_num)]
        for i in range(len(nums)):
            j = (nums[i] - m) // bucket
            s[j].append(nums[i])
        diff = 0
        x = max(s[0])
        for i in range(1, len(s)):
            if not s[i]:
                continue
            diff = max(diff, min(s[i]) - x)
            x = max(s[i])
        return diff


a = [1, 1, 1, 1]
Solution().maximumGap(a)
