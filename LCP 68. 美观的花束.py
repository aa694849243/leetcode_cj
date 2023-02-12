# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-02 23:59 
# ide： PyCharm
import collections

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        m = collections.defaultdict(int)
        p = 0
        ans = 0
        for i, v in enumerate(flowers):
            m[v] += 1
            while m[v] > cnt and p < i:
                m[flowers[p]] -= 1
                p += 1
            ans += i - p + 1
        return ans % (10 ** 9 + 7)


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().beautifulBouquet([1, 2, 3, 2], 1),
)

