'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# 数学 位运算 电路设计
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0

        for num in nums:
            # first appearance:
            # add num to seen_once
            # don't add to seen_twice because of presence in seen_once

            # second appearance:
            # remove num from seen_once
            # add num to seen_twice

            # third appearance:
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/single-number-ii/solution/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。singleNumber(self, nums: List[int]) -> int:
'''
@jinlinpang 这一题位运算的思路是K为奇数次的解法，实现是K=3的解法。K为偶数次的解法参考题目136。

思路是通用的，按照位运算的解题思路，k=5的解法如下：

public class SingleNumberSolution137 {

    public int singleNumber(int[] nums) {
        int seenOnce = 0, seenTwice = 0, seenThird = 0,seenForth = 0;
        for (int num : nums) {
            seenOnce = ~seenTwice & ~seenThird & ~seenForth & (seenOnce ^ num);//若seenTwice,seenThird,seenForth不改变，改变seenOnce
            seenTwice = ~seenOnce & ~seenThird & ~seenForth & (seenTwice ^ num);//若seenOnce,seenThird,seenForth不改变，改变seenTwice
            seenThird = ~seenOnce & ~seenTwice & ~seenForth & (seenThird ^ num);
            seenForth = ~ seenOnce & ~seenTwice & ~seenThird & (seenForth ^ num);
        }
        return seenOnce;
    }
}
'''
a=[3,3,3,2]
Solution().singleNumber(a)
