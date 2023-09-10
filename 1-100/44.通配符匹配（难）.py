# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        ans = 0
        n = len(height)
        for i, h in enumerate(height):
            while stk and height[stk[-1]] < h:
                top = stk.pop()
                if not stk:
                    break
                l, r = stk[-1], i
                ans += (min(height[l], height[r]) - height[top]) * (r - l - 1)
            stk.append(i)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
