'''给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。

示例 1:

输入: 12
输出: 21
示例 2:

输入: 21
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

import bisect


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = str(n)
        n = list(n)[::-1]
        for i in range(1, len(n)):
            if n[i] < n[i - 1]:
                x = bisect.bisect_right(n[:i], n[i])
                a = n[x]
                b = n[i]
                n[i] = a
                n[x] = b
                n = sorted(n.copy()[:i],reverse=True)+n[i:]
                ans=int(''.join(n)[::-1])
                return ans if ans<=2**31-1 else -1
        return -1


Solution().nextGreaterElement(154641284)
