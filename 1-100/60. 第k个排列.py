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
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i
        valid = [1] * (n + 1)
        ans = []
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    valid[j] = 0
                    ans.append(str(j))
                    break
            k %= factorial[n - i]
        return ''.join(ans)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
        visted = [0] * n
        res = []
        while k:
            resi = (k - 1) // (fact[n - len(res) - 1]) + 1
            k = k % fact[n - len(res) - 1]
            for i in range(n):
                if visted[i] == 0:
                    resi -= 1
                if resi == 0:
                    res.append(str(i + 1))
                    visted[i] = 1
                    break
            if k == 0:
                for i in range(n-1,-1,-1):
                    if visted[i] == 0:
                        res.append(str(i + 1))
        return ''.join(res)

# leetcode submit region end(Prohibit modification and deletion)
