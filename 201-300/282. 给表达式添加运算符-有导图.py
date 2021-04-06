'''给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加二元运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。

示例 1:

输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"]
示例 2:

输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]
示例 3:

输入: num = "105", target = 5
输出: ["1*0+5","10-5"]
示例 4:

输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]
示例 5:

输入: num = "3456237490", target = 9191
输出: []

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/expression-add-operators
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

import math


# 精妙递归 精妙回溯
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def backtrack(index, prev, cur, value, string):
            if index == n:
                if value == target and cur==0:
                    ans.append(''.join(string[1:]))
                return
            cur = cur * 10 + int(num[index])
            s = str(cur)
            if cur > 0:
                backtrack(index + 1, prev, cur, value, string)
            # +法
            string.append('+');
            string.append(s)
            backtrack(index + 1, cur, 0, value + cur, string)
            string.pop();
            string.pop()
            # 因为题目规定没有一元符号，所以*法和-法都不能+在开头
            if string:
                # -法
                string.append('-');
                string.append(s)
                backtrack(index + 1, -cur, 0, value - cur, string)
                string.pop();
                string.pop()
                # *法
                string.append('*');
                string.append(s)
                backtrack(index + 1, prev * cur, 0, value - prev + prev * cur, string)
                string.pop();
                string.pop()

        backtrack(0, 0, 0, 0, [])
        return ans

Solution().addOperators('1234567', 45)
