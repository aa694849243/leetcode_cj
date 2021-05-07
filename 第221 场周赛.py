# 5637. 判断字符串的两半是否相似
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        m = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        a = 0
        b = 0
        for i in s[:n // 2]:
            if i in m:
                a += 1
        for i in s[n // 2:]:
            if i in m:
                b += 1
        return a == b


# 5638. 吃苹果的最大数目
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        for i in range(len(apples)):
            if apples[i] != 0:
                break
        apples = apples[i:]
        days = days[i:]
        m = []
        m.append(min(days[0] - 1, apples[0] - 1))
        total = 0
        minus = 0

        for i in range(1, len(apples)):
            if apples[i] == 0:
                continue
            a = min(apples[i] + i - 1, days[i] + i - 1)
            if i > m[-1]:
                minus += i - m[-1] - 1
            if a > m[-1]:
                m.append(a)

        return m[-1] + 1 - minus


Solution().eatenApples([9, 10, 1, 7, 0, 2, 1, 4, 1, 7, 0, 11, 0, 11, 0, 0, 9, 11, 11, 2, 0, 5, 5], [3, 19, 1, 14, 0, 4, 1, 8, 2, 7, 0, 13, 0, 13, 0, 0, 2, 2, 13, 1, 0, 3, 7])
