'''给定一个整数 n, 返回从 1 到 n 的字典顺序。

例如，

给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lexicographical-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        lth = len(str(n))

        def dfs(x):
            if len(str(x))>=lth:
                return []
            l = []
            for i in range(10):
                object = int(str(x) + str(i))
                if object <= n:
                    l.append(object)
                    l.extend(dfs(int(str(x) + str(i))))
            return l
        for i in range(1,10):
            if i <= n:
                ans.append(i)
                ans.extend(dfs(int(str(i))))
        return ans
Solution().lexicalOrder(1)

