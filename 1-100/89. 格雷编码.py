'''
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。

格雷编码序列必须以 0 开头。

 

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1
示例 2:

输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
     给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
     因此，当 n = 0 时，其格雷编码序列为 [0]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gray-code
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# 找规律 镜像题
class Solution:
    def grayCode(self, n: int) -> List[int]:
        x = ['0']
        if n == 0:
            return [0]

        def dfs(x, n):
            if n == 0:
                return x
            y = []
            for i in x:
                y.append('0' + i)
            for j in range(len(x)-1, -1, -1):
                y.append('1' + x[j])
            return  dfs(y, n - 1)

        res = dfs(['0', '1'], n - 1)
        ans = [int(i, 2) for i in res]
        return ans


Solution().grayCode(3)
