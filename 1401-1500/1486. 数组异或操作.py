# 给你两个整数，n 和 start 。
#
#  数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。
#
#  请返回 nums 中所有元素按位异或（XOR）后得到的结果。
#
#
#
#  示例 1：
#
#  输入：n = 5, start = 0
# 输出：8
# 解释：数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
#      "^" 为按位异或 XOR 运算符。
#
#
#  示例 2：
#
#  输入：n = 4, start = 3
# 输出：8
# 解释：数组 nums 为 [3, 5, 7, 9]，其中 (3 ^ 5 ^ 7 ^ 9) = 8.
#
#  示例 3：
#
#  输入：n = 1, start = 7
# 输出：7
#
#
#  示例 4：
#
#  输入：n = 10, start = 5
# 输出：2
#
#
#
#
#  提示：
#
#
#  1 <= n <= 1000
#  0 <= start <= 1000
#  n == nums.length
#
#  Related Topics 位运算 数组
#  👍 76 👎 0

# 数学法 参照官方题解
# https://leetcode-cn.com/problems/xor-operation-in-an-array/solution/shu-zu-yi-huo-cao-zuo-by-leetcode-solution/
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def sumxor(x):  # 计算从0，1，2，3...x的异或和
            if x % 4 == 0:
                return x
            elif x % 4 == 1:
                return 1
            elif x % 4 == 2:
                return x + 1
            elif x % 4 == 3:
                return 0
            elif x < 0:
                return 0

        e = n & start & 1  # 只有start和n同为奇数最后结果才为奇数
        s = start // 2
        return (sumxor(s - 1) ^ sumxor(s - 1 + n)) * 2 | e


Solution().xorOperation(1, 7)
