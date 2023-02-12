# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 0:19 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            if a < 0:
                while stk and stk[-1] > 0 and stk[-1] < abs(a):
                    stk.pop()
                if stk and stk[-1] == abs(a):
                    stk.pop()
                elif not stk or stk[-1] < 0:
                    stk.append(a)
            else:
                stk.append(a)

        return stk
# leetcode submit region end(Prohibit modification and deletion)

