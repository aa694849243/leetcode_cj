# -*- coding: utf-8 -*-
from typing import List


# 给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
#
#  形式上，如果可以找出索引 i+1 < j 且满足 A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... +
# A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1] 就可以将数组三等分。
#
#
#
#  示例 1：
#
#  输入：[0,2,1,-6,6,-7,9,1,2,0,1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#
#
#  示例 2：
#
#  输入：[0,2,1,-6,6,7,9,-1,2,0,1]
# 输出：false
#
#
#  示例 3：
#
#  输入：[3,3,6,5,-2,2,5,1,-9,4]
# 输出：true
# 解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
#
#
#
#  提示：
#
#
#  3 <= A.length <= 50000
#  -10^4 <= A[i] <= 10^4
#
#  Related Topics 数组
#  👍 143 👎 0


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        a = sum(arr)
        target = a // 3
        if a / 3 != target:
            return False
        cum = 0
        cnt = 0
        for i in range(len(arr)):
            cum += arr[i]
            if cum == target:
                cnt += 1
                cum = 0
            if cnt == 2:
                break
        if i == len(arr) - 1:
            return False
        cum += sum(arr[i + 1:])
        if cum == target:
            cnt += 1
            cum = 0

        return cnt == 3 and cum == 0
