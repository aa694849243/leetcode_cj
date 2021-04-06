'''给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections


# 1动态规划
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = [1] * len(nums)
        cnt = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] >= length[i]:  # 发现前面序列长度比较高，可以更新长度同时更新cnt值
                        length[i] = length[j] + 1
                        cnt[i] = cnt[j]  # 数量与长度-1的数量相同
                    elif length[j] + 1 == length[i]:  # 发现某处+1长度后等于目前检测位置的长度,则更新数量，即加上原有数。
                        cnt[i] += cnt[j]
        longest = max(length)
        return sum(c for i, c in enumerate(cnt) if length[i] == longest)


# 2线段树 时间复杂度O(NlogN)
# 线段树二分 特殊二分
class Node:
    def __init__(self, left_range, right_range):
        self.val = (0, 1)
        self.left_range = left_range
        self.right_range = right_range
        self._left = self._right = None

    @property
    def mid_range(self):  # property创造属性类的方法
        return (self.right_range + self.left_range) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.left_range, self.mid_range)  # 等式的意思是找非None值
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid_range + 1, self.right_range)
        return self._right


class Solution:
    def merge(self, v1, v2):
        if v1[0] == v2[0]:  # 最长长度相同
            if v1[0] == 0: return (0, 1)  # 返回初始长度0
            return (v1[0], v1[1] + v2[1])  # 返回相同长度，合并数量
        return max(v1, v2)  # 返回长的那个

    def insert(self, node, key, val):  # 找到key对应的节点，插入val
        if node.left_range == node.right_range:  # 此时left_range==right_range==key
            node.val = self.merge(val, node.val)
            return
        if key <= node.mid_range:
            self.insert(node.left, key, val)
        else:
            self.insert(node.right, key, val)
        node.val = self.merge(node.left.val, node.right.val)

    def query(self, node, key):
        if key >= node.right_range:
            return node.val
        elif key < node.left_range:
            return (0, 1)
        return self.merge(self.query(node.left, key), self.query(node.right, key))

    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        root = Node(min(nums), max(nums))
        for num in nums:
            l, cnt = self.query(root, num - 1)
            self.insert(root, num, (l + 1, cnt))
        return root.val[1]


Solution().findNumberOfLIS([1, 3, 5, 4, 7])
