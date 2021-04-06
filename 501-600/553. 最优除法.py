'''给定一组正整数，相邻的整数之间将会进行浮点除法操作。例如， [2,3,4] -> 2 / 3 / 4 。

但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，才能得到最大的结果，并且返回相应的字符串格式的表达式。你的表达式不应该含有冗余的括号。

示例：

输入: [1000,100,10,2]
输出: "1000/(100/10/2)"
解释:
1000/(100/10/2) = 1000/((100/10)/2) = 200
但是，以下加粗的括号 "1000/((100/10)/2)" 是冗余的，
因为他们并不影响操作的优先级，所以你需要返回 "1000/(100/10/2)"。

其他用例:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
说明:

输入数组的长度在 [1, 10] 之间。
数组中每个元素的大小都在 [2, 1000] 之间。
每个测试用例只有一个最优除法解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/optimal-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1数学
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        for i in range(len(nums)):
            if i == 1:
                nums[i] = '(' + str(nums[i]) + '/'
            elif i == len(nums) - 1:
                nums[i] = str(nums[i]) + ')'
            else:
                nums[i] = str(nums[i]) + '/'
        return ''.join(nums)


# 2记忆化回溯
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        ma = {}
        mi = {}

        def backtrack(i, j):
            if (i, j) in ma:
                return ma[(i, j)], mi[(i, j)]
            if i == j:
                return str(nums[i]), str(nums[i])
            if j - i == 1:
                return str(nums[i]) + '/' + str(nums[j]), str(nums[i]) + '/' + str(nums[j])
            if j - i == 2:
                return str(nums[i]) + '/(' + str(nums[i + 1]) + '/' + str(nums[j]) + ')', str(nums[i]) + '/' + str(
                    nums[i + 1]) + '/' + str(nums[j])
            flagmax = 0
            flagmin = float('inf')
            ansmin = ''
            ansmax = ''
            for k in range(i, j):
                a, b = backtrack(i, k)
                c, d = backtrack(k + 1, j)
                e = eval(a + '/(' + d + ')')
                f = eval(b + '/' + d)
                if e > flagmax:
                    flagmax = e
                    ansmax = a + '/(' + d + ')'
                if f < flagmin:
                    flagmin = f
                    ansmin = b + '/' + d
            ma[(i, j)] = ansmax
            mi[(i, j)] = ansmin
            return ansmax, ansmin

        a,b=backtrack(0, len(nums) - 1)
        return a
Solution().optimalDivision([1000,100,10,2,55])