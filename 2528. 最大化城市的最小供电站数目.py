# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-01-31 20:54 
# ide： PyCharm
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        def check(x):
            q = collections.deque()
            sum_ = 0
            tmp = 0
            for i in range(r + 1):
                sum_ += stations[i]
                q.append(stations[i])
            if sum_ < x:
                q[-1] += x - sum_
                tmp += x - sum_
                sum_ = x
            for i in range(r + 1, len(stations)):
                if len(q) == 2 * r + 1:
                    sum_ -= q.popleft()
                if stations[i] + sum_ < x:
                    tmp += x - stations[i] - sum_
                    q.append(x - sum_)
                    sum_ = x
                else:
                    q.append(stations[i])
                    sum_ += stations[i]
            return tmp + max(0, x - sum(list(q)[-(r + 1):])) <= k

        left, right = 0, (2*r+1)*max(stations)+k+1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left if check(left) else left - 1


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().maxPower(
        [4, 4, 4, 4],
        0,
        3
    )
)

