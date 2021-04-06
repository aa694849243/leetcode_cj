'''给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
不允许旋转信封。

示例:

输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/russian-doll-envelopes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes or not envelopes[0]:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        def LIS(l):
            a = []
            for i in range(len(l)):
                if not a or l[i]>a[-1]:
                    a.append(l[i])
                else:
                    b=bisect.bisect_left(a,l[i])
                    a[b]=l[i]
            return len(a)

        return LIS([i[1] for i in envelopes])


a = [[1,1],[1,1],[1,1]]
Solution().maxEnvelopes(a)
