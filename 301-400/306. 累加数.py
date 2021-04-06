'''累加数是一个字符串，组成它的数字可以形成累加序列。

一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

示例 1:

输入: "112358"
输出: true
解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
示例 2:

输入: "199100199"
输出: true
解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
进阶:
你如何处理一个溢出的过大的整数输入?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/additive-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 回溯法
# 如果数字大，则利用字符串相加的方法
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        lenth = len(num)

        def backtrack(s, i, j, k):
            if s[i] == '0' and len(s[i:j]) > 1 or s[j] == '0' and len(s[j:k]) > 1: return False
            l = len(str(int(s[i:j]) + int(s[j:k])))
            if k + l <= lenth and int(s[i:j]) + int(s[j:k]) == int(s[k:k + l]):
                if k + l == lenth:
                    return True
                return backtrack(s, j, k, k + l)
            else:
                return False

        for i in range(1,lenth -1):
            for j in range(i + 1, lenth):
                if backtrack(num, 0, i, j):
                    return True
        return False


Solution().isAdditiveNumber("123")


# class Solution:
#     def isAdditiveNumber(self, num):
#         """
#         :type num: str
#         :rtype: bool
#         """
#
#         def recursion(i, j, k):
#             # 判断是否是01这种情况
#             if num[i] == '0' and j - i > 1 or num[j] == '0' and k - j > 1: return False
#             a = num[i:j]
#             b = num[j:k]
#             c = str(int(a) + int(b))
#             size = len(c)
#             if c != num[k:k + size]: return False
#             if k + size == len(num): return True
#             return recursion(j, k, k + size)
#
#         i = 0
#         size = len(num)
#         for j in range(i + 1, size):
#             for k in range(j + 1, size):
#                 if recursion(i, j, k): return True
#         return False
#
#
# Solution().isAdditiveNumber("11213")
