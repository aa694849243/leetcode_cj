'''神奇的字符串 S 只包含 '1' 和 '2'，并遵守以下规则：

字符串 S 是神奇的，因为串联字符 '1' 和 '2' 的连续出现次数会生成字符串 S 本身。

字符串 S 的前几个元素如下：S = “1221121221221121122 ......”

如果我们将 S 中连续的 1 和 2 进行分组，它将变成：

1 22 11 2 1 22 1 22 11 2 11 22 ......

并且每个组中 '1' 或 '2' 的出现次数分别是：

1 2 2 1 1 2 1 2 2 1 2 2 ......

你可以看到上面的出现次数就是 S 本身。

给定一个整数 N 作为输入，返回神奇字符串 S 中前 N 个数字中的 '1' 的数目。

注意：N 不会超过 100,000。

示例：

输入：6
输出：3
解释：神奇字符串 S 的前 6 个元素是 “12211”，它包含三个 1，因此返回 3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/magical-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

# 1模拟法
import collections
class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 3:
            return 1
        a1 = [1, 2] + [0] * (n - 2)
        a2 = [1, 2, 2]
        i = 2
        while len(a2) < n:
            a1[i] = a2[i]
            a2.extend([3 - a2[-1]] * a1[i])
            i += 1
        return collections.Counter(a2[:n])[1]
