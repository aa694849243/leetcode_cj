'''给定一个包含 非负数 的数组和一个目标 整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，且总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。

 

示例 1：

输入：[23,2,4,6,7], k = 6
输出：True
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6。
示例 2：

输入：[23,2,6,4,7], k = 6
输出：True
解释：[23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
 

说明：

数组的长度不会超过 10,000 。
你可以认为所有数字总和在 32 位有符号整数范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/continuous-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

# 1数学
# https://leetcode-cn.com/problems/continuous-subarray-sum/solution/lian-xu-de-zi-shu-zu-he-by-leetcode/
# 方法三
import itertools


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        flag = 0
        for num in nums:
            if num == 0:
                flag += 1
            else:
                flag = 0
            if flag == 2:  # 出现连续两个0的情况一定为True
                return True
        precum = [*itertools.accumulate(nums)]
        m = {0: -1}
        if k == 0:
            for i in range(len(precum)):
                if precum[i] in m and i - m[precum[i]] >= 2:
                    return True
                if precum[i] not in m:  # 不更新，让i保持最远
                    m[precum[i]] = i
            return False
        for i in range(len(precum)):
            num = precum[i] % k  # 求余数
            if num in m and i - m[num] >= 2:  # 余数在字典里即可
                return True
            if num not in m:
                m[num] = i
        return False


Solution().checkSubarraySum([1, 0], 2)
