# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 0:11 
# ide： PyCharm
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk_num = []
        for a in tokens:
            if a in ['+', '-', '*', '/']:
                if len(stk_num) >= 2:
                    b = stk_num.pop()
                    c = stk_num.pop()
                    if a == '+':
                        stk_num.append(c + b)
                    elif a == '-':
                        stk_num.append(c - b)
                    elif a == '*':
                        stk_num.append(c * b)
                    else:
                        stk_num.append(int(c/b))
            else:
                stk_num.append(int(a))
        return stk_num[0]
# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().evalRPN(
        ["4","13","5","/","+"]
    )
)
