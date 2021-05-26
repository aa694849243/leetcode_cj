import bisect
import collections, heapq, itertools
from typing import List


# 5742. 将句子排序
class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        li = [''] * len(s)
        for word in s:
            li[int(word[-1]) - 1] = word[:-1]
        return ' '.join(li)


# 5743. 增长的内存泄露
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        q = [(-memory1, 1), (-memory2, 2)]
        heapq.heapify(q)
        ans = [-1] * 3
        for i in range(1, 2 ** 31):
            a, id = heapq.heappop(q)
            a *= -1
            if i > a and not q:
                ans[id] = a
                ans[0] = i
                break
            elif i > a and q:
                ans[id] = a
                a_, id_ = heapq.heappop(q)
                a_ *= -1
                if i > a_:
                    ans[id_] = a_
                    ans[0] = i
                    break
                elif i == a_:
                    ans[id_] = 0
                    ans[0] = i + 1
                    break
                else:
                    a_ -= i
                    heapq.heappush(q, (-a_, id_))
            a -= i
            if a == 0:
                ans[id] = 0
                if not q:
                    ans[0] = i + 1
            else:
                heapq.heappush(q, (-a, id))
        return ans


Solution().memLeak(9, 6)


# 5744. 旋转盒子
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i, row in enumerate(box):
            l, r = 0, len(row)
            cnt = 0
            flag = 0
            while l < r:
                if row[l] == '*' or l == r - 1:
                    if l != r - 1:
                        row[l - cnt:l] = ['#'] * cnt
                        row[flag:l - cnt] = ['.'] * len(row[flag:l - cnt])
                        cnt = 0
                        flag = l + 1
                    else:
                        if row[r - 1] == '#':
                            cnt += 1
                        elif row[r - 1] == '*':
                            row[l - cnt:l] = ['#'] * cnt
                            row[flag:l - cnt] = ['.'] * len(row[flag:l - cnt])
                            break
                        row[r - cnt:r] = ['#'] * cnt
                        row[flag:r - cnt] = ['.'] * len(row[flag:r - cnt])
                        cnt = 0
                        flag = l + 1

                elif row[l] == '#':
                    cnt += 1
                l += 1
            box[i] = row
        li = []
        for r in zip(*box):
            li.append(list(r)[::-1])
        return li


# 5212. 向下取整数对和


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        nums.sort()
        ans = 0
        m = {}
        for i, num in enumerate(nums):
            if i == 0 or i > 0 and num != nums[i - 1]:
                left = i
            for mul in range(1, nums[-1] // num + 1):
                t1, t2 = num * mul, num * (mul + 1)
                if t1 in m:
                    L = m[t1]
                else:
                    L = bisect.bisect_left(nums, t1, left)
                    m[t1] = L
                if t2 in m:
                    R = m[t2]
                else:
                    R = bisect.bisect_left(nums, t2, left)
                ans += mul * (R - L)
                ans %= mod
        return ans


Solution().sumOfFlooredPairs([7,7,7,7,7,7,7])
