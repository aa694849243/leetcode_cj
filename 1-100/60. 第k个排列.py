'''
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 参考https://leetcode-cn.com/problems/permutation-sequence/solution/di-k-ge-pai-lie-by-leetcode/
# 阶乘数系统
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        f_permutation = [str(i + 1) for i in range(n)]  # 最低序列表
        factorials = [0]
        j = 1
        for i in range(1, n):
            j *= i
            factorials.append(j)
        k -= 1
        ans = ''
        for l in range(n - 1, 0, -1):
            idx = k // factorials[l]
            ans += f_permutation.pop(idx)
            k -= idx * factorials[l]
        ans += f_permutation[0]
        return ans



n = 4
k = 9
Solution().getPermutation(n, k)
