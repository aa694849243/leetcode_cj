from typing import List
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        lst = [(x[0], i, 0) for i, x in enumerate(nums)]
        lst.sort()
        mi, ma = lst[0][0], lst[-1][0]
        diff_mi = ma - mi
        ans = [mi, ma]
        heapq.heapify(lst)
        while True:
            x, r, c = heapq.heappop(lst)
            if c + 1 == len(nums[r]):
                break
            nxt = nums[r][c + 1]
            heapq.heappush(lst, (nxt, r, c + 1))
            ma = max(ma, nxt)
            if ma - lst[0][0] < diff_mi:
                diff_mi = ma - lst[0][0]
                ans = [lst[0][0], ma]
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
)
