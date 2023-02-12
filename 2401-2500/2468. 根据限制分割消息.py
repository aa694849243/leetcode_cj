# -*- coding: utf-8 -*-
# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/split-message-based-on-limit/solution/mei-ju-by-endlesscheng-gt7c/
class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        cap = 0
        n = len(message)
        i = 0
        while 1:
            i += 1
            if i < 10:
                tail = 5
            elif i < 100:
                if i == 10:
                    cap -= 9
                tail = 7
            elif i < 1000:
                if i == 100:
                    cap -= 99
                tail = 9
            else:
                if i == 1000:
                    cap -= 999
                tail = 11
            if tail >= limit:
                return []
            cap += limit - tail
            if cap < n:
                continue
            res = []
            p = 0
            for num in range(1, i + 1):
                tmp = f'<{num}/{i}>'
                res.append(message[p:p + limit - len(tmp)] + tmp)
                p += limit - len(tmp)
            return res

# leetcode submit region end(Prohibit modification and deletion)
