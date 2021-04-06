'''给定一个正整数 n，你可以做如下操作：

1. 如果 n 是偶数，则用 n / 2替换 n。
2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
n 变为 1 所需的最小替换次数是多少？

示例 1:

输入:
8

输出:
3

解释:
8 -> 4 -> 2 -> 1
示例 2:

输入:
7

输出:
4

解释:
7 -> 8 -> 4 -> 2 -> 1
或
7 -> 6 -> 3 -> 2 -> 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-replacement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
# 1 递归
import functools


class Solution:
    def integerReplacement(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(n):
            if n == 1:
                return 0
            if not n % 2:
                return 1 + dfs(n // 2)
            else:
                return min(1 + dfs(n + 1), 1 + dfs(n - 1))

        return dfs(n)


# 2 递归+备忘录 记忆化搜索
class Solution:
    def integerReplacement(self, n: int) -> int:
        mem = {1: 0}

        def dfs(n):
            if n in mem:
                return mem[n]
            if not n % 2:
                ans = 1 + dfs(n // 2)
            else:
                ans = 1 + min(dfs(n + 1), dfs(n - 1))
            mem[n] = ans
            return ans

        return dfs(n)


# 3 数学
##1偶数直接右移，只有一种选项
##2 奇数+1或者-1，有两种选项。
###2.1 显然，让每一步1的数目最少好处大，于是 0bxxx01 采用 -1； 0bxxx11 采用 +1；
### 2.2 特殊情况 3，按上述原则+1后两次右移共需3次；减一后只需一次右移共2次，因此3采用-1操作
class Solution:
    def integerReplacement(self, n: int) -> int:
        i = 0
        while n > 1:
            if n & 1:
                if n != 3 and n & 3 == 3:
                    n += 1
                else:
                    n -= 1
            else:
                n >>= 1
            i+=1
        return i