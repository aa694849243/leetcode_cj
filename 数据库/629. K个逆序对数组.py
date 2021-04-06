'''给出两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个逆序对的不同的数组的个数。

逆序对的定义如下：对于数组的第i个和第 j个元素，如果满i < j且 a[i] > a[j]，则其为一个逆序对；否则不是。

由于答案可能很大，只需要返回 答案 mod 109 + 7 的值。

示例 1:

输入: n = 3, k = 0
输出: 1
解释:
只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。
示例 2:

输入: n = 3, k = 1
输出: 2
解释:
数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。
说明:

 n 的范围是 [1, 1000] 并且 k 的范围是 [0, 1000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-inverse-pairs-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# f(i, j) = f(i, j - 1) + f(i - 1, j) - f(i - 1, j - i)
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        m = 10 ** 9 + 7
        f = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    f[i][j] = 1
                elif i == 1:  # 只有f[1][0]=1，其他f[1][j]全部等于0
                    f[i][j] = 0
                elif j >= i:
                    f[i][j] = (f[i][j - 1] + f[i - 1][j] - f[i - 1][j - i]) % m
                else:
                    f[i][j] = (f[i][j - 1] + f[i - 1][j]) % m
        return f[-1][-1]


Solution().kInversePairs(3, 3)
