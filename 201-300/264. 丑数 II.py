'''编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# 堆
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        seen = {1, }
        heapq.heappush(heap, 1)
        count = n
        ans = []
        while count != 0:
            num = heapq.heappop(heap)
            for i in [2, 3, 5]:
                if num * i not in seen:
                    seen.add(num * i)
                    heapq.heappush(heap, num * i)
            ans.append(num)
            count -= 1
        return num


# 动态规划
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        i2 = i3 = i5 = 0
        for i in range(1, n):
            dp[i] = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)

            if dp[i] == dp[i2]*2:
                i2 += 1
            if dp[i] == dp[i3]*3:
                i3 += 1
            if dp[i]==dp[i5]*5:
                i5 += 1
        return dp[-1]
Solution().nthUglyNumber(11)


class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0

        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1


class Solution:
    u = Ugly()

    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]



Solution().nthUglyNumber(11)
