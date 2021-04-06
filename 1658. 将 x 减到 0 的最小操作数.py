'''给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。

如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

 

示例 1：

输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
示例 2：

输入：nums = [5,6,7,8,9], x = 4
输出：-1
示例 3：

输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1滑动窗口 caojie
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0
        l = r = 0  # 左右窗口边界
        accum = 0
        ans = float('inf')
        while l < len(nums) and r - l + 1 <= len(nums):  # r可以适当延长，只要窗口大小不超过数组长度就行了
            accum += nums[r % len(nums)]  # 将右边界的值加入
            if l == 0 or r >= len(nums) - 1:  # 左边界在原点或右边界超过数组长度说明符合题目条件，即要么只取左边一截，或取右边一截，或左右各一截
                if accum == x:
                    ans = min(ans, r - l + 1)
                elif accum > x:  # 收缩窗口
                    while l < len(nums) and accum > x:
                        accum -= nums[l]
                        l += 1
                    if accum == x and r >= len(nums) - 1:  # 收缩窗口过程满足条件，将结果加入ans比对
                        ans = min(ans, r - l + 1)
            r += 1
        return ans if ans != float('inf') else -1


# 2哈希表+前缀和
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        lprecum = [nums[0]]
        rprecum = [nums[-1]]
        for i in range(1, len(nums)):
            lprecum.append(lprecum[-1] + nums[i])
            rprecum.append(rprecum[-1] + nums[-1 - i])
        ml = {lprecum[i]: i for i in range(len(lprecum) - 1, -1, -1)}
        mr = {rprecum[i]: i for i in range(len(rprecum) - 1, -1, -1)}  # 倒着加防止相同的前缀和后面覆盖前面
        ans = min(ml.get(x, float('inf')), mr.get(x, float('inf'))) + 1
        for i, j in enumerate(lprecum):
            if x-j in mr and i+1+mr[x-j]+1<len(nums):
                ans = min(ans, i + 1 + mr[x-j] + 1)
        return ans if ans != float('inf') else -1


Solution().minOperations([3,2,20,1,1,3], 10)
