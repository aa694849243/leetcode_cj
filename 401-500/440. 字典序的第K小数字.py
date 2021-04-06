'''给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。

注意：1 ≤ k ≤ n ≤ 109。

示例 :

输入:
n: 13   k: 2

输出:
10

解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 十叉树
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def cal_step(n, n1, n2):  # n1到n2需要走多少步
            steps = 0
            while n1 <= n:
                steps += min(n2, n + 1)-n1
                n1 *= 10
                n2 *= 10
            return steps

        cur = 1
        k -= 1  # k-1相当于先走一步
        while k > 0:
            steps = cal_step(n, cur, cur + 1)
            if k - steps >= 0: #往右走一步需要付出的步数
                cur += 1
                k -= steps
            else: #不能往右走，往下走一步后（k-1）再计算
                cur *= 10
                k -= 1
        return cur
Solution().findKthNumber(2,2)
