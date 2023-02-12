# -*- coding: utf-8 -*-
# datetime： 2023-02-04 0:15
# ide： PyCharm
import copy

# leetcode submit region begin(Prohibit modification and deletion)
# 连分数
# https://leetcode.cn/problems/XxZZjK/solution/zhao-gui-lu-han-jie-fa-de-zheng-ming-by-m43kf/
# 找规律
# https://leetcode.cn/problems/XxZZjK/solution/czhao-gui-lu-jian-dan-yi-dong-by-teng-s-smm9/
tem = [[],
       [[1, 1]],
       [[1, 1], [2, 1], [2, 3]],
       [[1, 1], [2, 2], [3, 1], [3, 3], [3, 5]],
       [[1, 1], [2, 3], [3, 2], [4, 1], [4, 3], [4, 5], [4, 7]]
       ]


class Solution:
    def sandyLandManagement(self, size: int) -> List[List[int]]:
        if size <= 4:
            return copy.deepcopy(tem[size])
        res = self.sandyLandManagement(size - 4)
        res.extend([[size, 2 * i + 1] for i in range(size)])
        res.append([size - 1, 2])
        res.extend([[size-2, 2 * i + 1] for i in range(1,size - 2)])
        res.append([size - 3, 1])
        return res
# leetcode submit region end(Prohibit modification and deletion)

