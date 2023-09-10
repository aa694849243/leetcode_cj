# 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回
# 所有 能够得到 target 的表达式。
#
#  注意，返回表达式中的操作数 不应该 包含前导零。
#
#
#
#  示例 1:
#
#
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"]
# 解释: “1*2*3” 和 “1+2+3” 的值都是6。
#
#
#  示例 2:
#
#
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"]
# 解释: “2*3+2” 和 “2+3*2” 的值都是8。
#
#
#  示例 3:
#
#
# 输入: num = "3456237490", target = 9191
# 输出: []
# 解释: 表达式 “3456237490” 无法得到 9191 。
#
#
#
#
#  提示：
#
#
#  1 <= num.length <= 10
#  num 仅含数字
#  -2³¹ <= target <= 2³¹ - 1
#
#
#  Related Topics 数学 字符串 回溯
#  👍 448 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def back_track(i, prev, cur, val, path):
            cur = cur * 10 + int(num[i])
            if i == n - 1:
                if path[-1] == '+' and val + cur == target:
                    res.append(''.join(path[1:] + [str(cur)]))
                elif path[-1] == '-' and val - cur == target:
                    res.append(''.join(path[1:] + [str(cur)]))
                elif path[-1] == '*' and val - prev + cur * prev == target:
                    res.append(''.join(path[1:] + [str(cur)]))
                return
            if cur != 0:
                back_track(i + 1, prev, cur, val, path)

            # 截断
            if path[-1] == '+':
                back_track(i + 1, cur, 0, val + cur, path + [str(cur), '+'])
                back_track(i + 1, cur, 0, val + cur, path + [str(cur), '-'])
                back_track(i + 1, cur, 0, val + cur, path + [str(cur), '*'])
            elif path[-1] == '-':
                back_track(i + 1, -cur, 0, val - cur, path + [str(cur), '+'])
                back_track(i + 1, -cur, 0, val - cur, path + [str(cur), '-'])
                back_track(i + 1, -cur, 0, val - cur, path + [str(cur), '*'])
            elif path[-1] == '*':
                back_track(i + 1, cur * prev, 0, val - prev + cur * prev, path + [str(cur), '+'])
                back_track(i + 1, cur * prev, 0, val - prev + cur * prev, path + [str(cur), '-'])
                back_track(i + 1, cur * prev, 0, val - prev + cur * prev, path + [str(cur), '*'])

        back_track(0, 0, 0, 0, ['+'])
        return res


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().addOperators('232', 6))
