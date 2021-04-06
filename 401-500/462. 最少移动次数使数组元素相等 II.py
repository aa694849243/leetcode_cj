'''给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。

例如:

输入:
[1,2,3]

输出:
2

说明：
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）：

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii/solution/zui-shao-yi-dong-ci-shu-shi-shu-zu-yuan-su-xiang-2/
# 找中位数
# 1 O(nlogn)方法
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        moves = 0
        mid = (len(nums) - 1) // 2
        for i in range(len(nums)):
            moves += abs(nums[mid] - nums[i])
        return moves


# 2快速选择
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def oneqsort(left, right):
            j = left
            pivot = nums[left]
            for i in range(left + 1, right + 1):
                if nums[i] < pivot:
                    j += 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[left], nums[j] = nums[j], nums[left]
            return j

        if len(nums) < 2:
            return 0
        left, right = 0, len(nums) - 1
        mid = right // 2
        while True:
            x = oneqsort(left, right)
            if x == mid:
                break
            elif x > mid:
                right = x - 1
            elif x < mid:
                left = x + 1
        moves = 0
        for i in range(len(nums)):
            moves += abs(nums[i] - nums[mid])
        return moves


Solution().minMoves2([1, 2, 3, 8])
