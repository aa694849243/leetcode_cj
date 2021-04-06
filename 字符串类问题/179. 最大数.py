'''
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

#自定义排序 魔法方法
class custom(str):
    def __lt__(self, other):
        return self + other < other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a = sorted(map(str, nums), key=custom,reverse=True)
        return ''.join(a) if a[0] != '0' else '0'


a = [121, 12]
Solution().largestNumber(a)
