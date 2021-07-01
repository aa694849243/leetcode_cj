# -*- coding: utf-8 -*-
from typing import List


# 给你一个整数数组 digits，你可以通过按任意顺序连接其中某些数字来形成 3 的倍数，请你返回所能得到的最大的 3 的倍数。
#
#  由于答案可能不在整数数据类型范围内，请以字符串形式返回答案。
#
#  如果无法得到答案，请返回一个空字符串。
#
#
#
#  示例 1：
#
#  输入：digits = [8,1,9]
# 输出："981"
#
#
#  示例 2：
#
#  输入：digits = [8,6,7,1,0]
# 输出："8760"
#
#
#  示例 3：
#
#  输入：digits = [1]
# 输出：""
#
#
#  示例 4：
#
#  输入：digits = [0,0,0,0,0,0]
# 输出："0"
#
#
#
#
#  提示：
#
#
#  1 <= digits.length <= 10^4
#  0 <= digits[i] <= 9
#  返回的结果不应包含不必要的前导零。
#
#  Related Topics 贪心 数组 动态规划
#  👍 52 👎 0


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        cnt = [0] * 10
        mod = [0] * 3
        for num in digits:
            cnt[num] += 1
            mod[num % 3] += 1
        s = sum(digits)
        del_mod, del_num = [0, 0]
        if s % 3 == 1:
            if mod[1] > 0:
                del_mod, del_num = 1, 1
            else:
                del_mod, del_num = 2, 2
        elif s % 3 == 2:
            if mod[2] > 0:
                del_mod, del_num = 2, 1
            else:
                del_mod, del_num = 1, 2
        ans=''
        for i in range(10):
            if del_num>0 and i%3==del_mod:
                if cnt[i]>=del_num:
                    cnt[i]-=del_num
                    del_num=0
                else:
                    del_num-=cnt[i]
                    cnt[i]=0
            ans+=str(i)*cnt[i]
        if ans and ans[-1]=='0':
            return '0'
        return ans[::-1]


Solution().largestMultipleOfThree([5,8])
