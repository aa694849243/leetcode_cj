'''
在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。

如果存在则返回 true，不存在返回 false。

 

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

# 二叉搜索树 自平衡二叉搜索树 AVL树

from bintrees import avltree


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) < 2:
            return False
        b = avltree.AVLTree()
        b.insert(nums[0], 0)
        for i in range(1, len(nums)):
            if i > k:
                b.remove(nums[i - k - 1])
            if (b.min_key() <= nums[i] and nums[i] - b.floor_key(nums[i]) <= t) or (
                    b.max_key() >= nums[i] and b.ceiling_key(nums[i]) - nums[i] <= t):
                return True
            b.insert(nums[i], i)
        return False


from collections import defaultdict

#桶
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k<=0 or t<0:
            return False
        s = defaultdict(list)
        size = t + 1
        for i in range(len(nums)):
            if i > k:
                s[nums[i - k - 1] // size] = []
            m = nums[i] // size
            if s[m]:
                return True
            elif s[m-1] and nums[i]-s[m-1][0]<=t or s[m+1] and s[m+1][0]-nums[i]<=t: #每个桶里如果超过一个元素，则直接会返回True
                return True
            s[m].append(nums[i])
        return False


nums = [2,1,9,6,8,7]; k = 1; t = 1
Solution().containsNearbyAlmostDuplicate(nums, k, t)
