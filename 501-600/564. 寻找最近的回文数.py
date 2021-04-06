'''给定一个整数 n ，你需要找到与它最近的回文数（不包括自身）。

“最近的”定义为两个整数差的绝对值最小。

示例 1:

输入: "123"
输出: "121"
注意:

n 是由字符串表示的正整数，其长度不超过18。
如果有多个结果，返回最小的那个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-closest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1数学法
# 方法二 https://leetcode-cn.com/problems/find-the-closest-palindrome/solution/xun-zhao-zui-jin-de-hui-wen-shu-by-leetcode/
# 简化版 https://leetcode-cn.com/problems/find-the-closest-palindrome/solution/jian-hua-guan-fang-ti-jie-de-si-lu-by-ming-ye/
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def mirror(n):
            half = n[:len(n) // 2]
            if len(n) % 2:  # 奇数长度
                return half + n[len(n) // 2] + half[::-1]
            else:
                return half + half[::-1]

        def getsmall(n):
            half = n[:len(n) // 2 + 1]  # 包括中间数字
            if len(n) % 2:  # 奇数情况
                half_new = str(int(half) - 1)
                if len(half_new) == len(half):  # 长度不变
                    return half_new + half_new[:-1][::-1]
                else:
                    return half_new + half_new[::-1]
            else:  # 偶数情况
                half_new = str(int(half[:-1]) - 1)
                if half_new == '0':
                    return '9'
                elif len(half_new) < len(half) - 1:  # 减少了位数
                    return '9' * (len(n) - 1)  # 减少了位数只有可能是999...
                else:
                    return half_new + half_new[::-1]

        def getbig(n):
            half = n[:len(n) // 2 + 1]  # 包括中间数字
            if len(n) % 2:  # 奇数情况
                half_new = str(int(half) + 1)
                if len(half_new) == len(half): #长度不变
                    return half_new + half_new[:-1][::-1]
                else: #增加了1位
                    return half_new[:-1] + half_new[:-1][::-1]
            else:
                half_new = str(int(half[:-1]) + 1)
                if len(half_new) == len(half):  # 增加了1位
                    return half_new + half_new[:-1][::-1]
                else:
                    return half_new + half_new[::-1]

        if n == 0:
            return '1'
        if len(n) == 1:
            return str(int(n) - 1)
        mir = mirror(n)
        a = getsmall(n)
        b = getbig(n)
        if mir == n:
            return a if abs(int(a) - int(n)) <= abs(int(b) - int(n)) else b
        else:
            c_dif = abs(int(mir) - int(n))
            a_dif = abs(int(a) - int(n))
            b_dif = abs(int(b) - int(n))
            x = min(a_dif, b_dif, c_dif)
            if a_dif == x:
                return a
            elif c_dif == x:
                return mir
            else:
                return b


Solution().nearestPalindromic("999")
