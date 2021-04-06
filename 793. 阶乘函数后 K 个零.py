''' f(x) 是 x! 末尾是 0 的数量。（回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 ）

例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。给定 K，找出多少个非负整数 x ，能满足 f(x) = K 。

 

示例 1：

输入：K = 0
输出：5
解释：0!, 1!, 2!, 3!, and 4! 均符合 K = 0 的条件。
示例 2：

输入：K = 5
输出：0
解释：没有匹配到这样的 x!，符合 K = 5 的条件。
 

提示：

K 是范围在 [0, 10^9] 的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        def cal(num):
            if num < 5:
                return 0
            ans = 0
            de = 5
            while num >= de:
                ans += (num // de)
                de *= 5
            return ans

        l, r = 0, 10 ** 10 + 1
        while l < r:
            mid = (l + r) // 2
            if cal(mid) < K:
                l = mid + 1
            else:
                r = mid
        if cal(l) != K:
            return 0
        x0 = l
        l, r = 0, 10 ** 10 + 1
        while l < r:
            mid = (l + r) // 2
            if cal(mid) < K + 1:
                l = mid + 1
            else:
                r = mid
        x1 = l
        return x1 - x0


Solution().preimageSizeFZF(10**9)


