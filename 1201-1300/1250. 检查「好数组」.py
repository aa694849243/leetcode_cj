# -*- coding: utf-8 -*-
from typing import List


# 给你一个正整数数组 nums，你需要从中任选一些子集，然后将子集中每一个数乘以一个 任意整数，并求出他们的和。
#
#  假如该和结果为 1，那么原数组就是一个「好数组」，则返回 True；否则请返回 False。
#
#
#
#  示例 1：
#
#  输入：nums = [12,5,7,23]
# 输出：true
# 解释：挑选数字 5 和 7。
# 5*3 + 7*(-2) = 1
#
#
#  示例 2：
#
#  输入：nums = [29,6,10]
# 输出：true
# 解释：挑选数字 29, 6 和 10。
# 29*1 + 6*(-3) + 10*(-1) = 1
#
#
#  示例 3：
#
#  输入：nums = [3,6]
# 输出：false
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10^5
#  1 <= nums[i] <= 10^9
#
#  Related Topics 数学
#  👍 22 👎 0
# 贝祖定理 裴蜀定理： 若 a,b 是整数,且 gcd(a,b)=d，那么对于任意的整数 x,y,ax+by 都一定是 d 的倍数，特别地，一定存在整数 x,y，使 ax+by=d 成立。
# 推论： a,b 互质的充分必要条件是存在整数 x,y 使 ax+by=1 。
#
# 分析题目，可知 [好数组] 的定义为存在一个子集其中的数字是互质的，即我们只要找出一个子集的最大公约数为 1 就能确保它为 [好数组]。
#
# 作者：Jweier
# 链接：https://leetcode-cn.com/problems/check-if-it-is-a-good-array/solution/pei-shu-ding-li-by-jweier-0lgi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/check-if-it-is-a-good-array/solution/pei-shu-ding-li-by-run916/
# https://leetcode-cn.com/problems/check-if-it-is-a-good-array/solution/shu-xue-he-365-shui-hu-wen-ti-lei-si-python-by-fe-/
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)
        a=nums[0]
        for b in nums[1:]:
            a=gcd(a,b)
        return a==1
