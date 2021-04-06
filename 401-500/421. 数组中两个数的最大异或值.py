'''给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 231 。

找到 ai 和aj 最大的异或 (XOR) 运算结果，其中0 ≤ i,  j < n 。

你能在O(n)的时间解决这个问题吗？

示例:

输入: [3, 10, 5, 25, 2, 8]

输出: 28

解释: 最大的结果是 5 ^ 25 = 28.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 字典树 前缀树 异或关键原理
# https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/solution/shu-zu-zhong-liang-ge-shu-de-zui-da-yi-huo-zhi-by-/
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        lookup = {}
        l = len(bin(max(nums))) - 2
        new_ = ['0' * (l - len(bin(num)[2:])) + bin(num)[2:] for num in nums]
        ans = 0
        for num in new_:
            trie = lookup
            xortrie = trie  # 异或字典树与字典树同步
            curmax = 0
            for node in num:  # 建立字典树
                if node not in trie:
                    trie[node] = {}
                trie = trie[node]
                xornode = str(1 - int(node))
                if xornode in xortrie:  # 每加入一个数都与之前的字典树比较，是否存在更大的可能
                    xortrie = xortrie[xornode]
                    curmax = (curmax << 1) | 1
                else:
                    xortrie = xortrie[node]
                    curmax <<= 1
            ans = max(curmax, ans)
        return ans


Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
