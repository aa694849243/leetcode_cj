'''给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:

输入: [1,2,3,4,5]
输出: true
示例 2:

输入: [5,4,3,2,1]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-triplet-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
# 1. 设置两个指针m1（代表最小值）,m2（代表第二小的值），初始化m1为nums[0],m2为float('inf')
# 2. 当出现一个数大于m1，则将其保存为m2，即出现m2后数组递增长度为2
# 3. 当出现一个数小于等于m1，更新m1为最小值
# 4. 当出现一个数大于m1但小于m2，更新m2
# 5. 当出现一个数大于m2，返回真

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        m1 = nums[0]
        m2=float('inf')
        for i in range(1, len(nums)):
            if nums[i] > m2:
                return True
            elif nums[i] > m1:
                m2 = nums[i]
            elif nums[i] <= m1:
                m1 = nums[i]

        return False


a = [1, 0, 1, 0, 0, 100]
Solution().increasingTriplet(a)
