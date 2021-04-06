'''给定两个整数 n 和 k，你需要实现一个数组，这个数组包含从 1 到 n 的 n 个不同整数，同时满足以下条件：

① 如果这个数组是 [a1, a2, a3, ... , an] ，那么数组 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数；.

② 如果存在多种答案，你只需实现并返回其中任意一种.

示例 1:

输入: n = 3, k = 1
输出: [1, 2, 3]
解释: [1, 2, 3] 包含 3 个范围在 1-3 的不同整数， 并且 [1, 1] 中有且仅有 1 个不同整数 : 1
 

示例 2:

输入: n = 3, k = 2
输出: [1, 3, 2]
解释: [1, 3, 2] 包含 3 个范围在 1-3 的不同整数， 并且 [2, 1] 中有且仅有 2 个不同整数: 1 和 2
 

提示:

 n 和 k 满足条件 1 <= k < n <= 104.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/beautiful-arrangement-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        a = []
        for i in range(1, n - k + 1):
            a.append(i)
        b = [0] * k
        l, r = 0, 1
        for i in range(n, n - k, -1):
            if l <= len(b) - 1:
                b[l] = i
                l += 2
            else:
                break
        for i in range(n - k + 1, n + 1):
            if r <= len(b) - 1:
                b[r] = i
                r += 2
            else:
                break
        return a + b
