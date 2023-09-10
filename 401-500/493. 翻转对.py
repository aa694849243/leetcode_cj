'''给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3
注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1归并 超时
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.li = [0] * (n + 1)

    @staticmethod
    def lowbit(num):
        return num & -num

    def update(self, num, dt):
        while num <= self.n:
            self.li[num] += dt
            num += self.lowbit(num)

    def query(self, num):
        res = 0
        while num > 0:
            res += self.li[num]
            num -= self.lowbit(num)
        return res


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 离散化
        s = set(nums)
        for num in nums:
            s.add(num * 2)
        s = sorted(s)
        ranks = {num: rank + 1 for rank, num in enumerate(s)}
        ftree = FenwickTree(len(ranks))
        ans = 0
        for num in nums[::-1]:
            ans += ftree.query(ranks[num] - 1)
            ftree.update(ranks[num * 2], 1)
        return ans

