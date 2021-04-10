'''在一根无限长的数轴上，你站在0的位置。终点在target的位置。

每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。

返回到达终点需要的最小移动次数。

示例 1:

输入: target = 3
输出: 2
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 3 。
示例 2:

输入: target = 2
输出: 3
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 -1 。
第三次移动，从 -1 到 2 。
注意:

target是在[-10^9, 10^9]范围中的非零整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reach-a-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 数学 奇偶问题，当gap为偶数时，只需要将gap//2变为负数即可，当gap为奇数时,序列是两奇数两偶数这样排列，那么gap+step如果仍为奇数，那么gap+step+step+1一定为偶数
class Solution:
    def reachNumber(self, target: int) -> int:
        l = 0
        target = abs(target)
        step = 1
        while l <= target:
            if l == target:
                return step - 1
            else:
                l += step
                step += 1
        gap = l - target
        if gap % 2 == 0:
            return step - 1
        elif (gap + step) % 2 == 0:
            return step
        else:
            return step + 1


Solution().reachNumber(2)
