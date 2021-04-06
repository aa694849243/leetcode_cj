'''
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
通过次数88,685提交次数168,006

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        l = len(b)
        l2 = len(a)
        b = '0' * (l2 - l) + b
        ans = ['0'] * l2
        c = 0
        for i in range(l2 - 1, -1, -1):
            if int(a[i]) + int(b[i]) + c == 2:
                ans[i] = '0'
                c = 1
            elif int(a[i]) + int(b[i]) + c == 3:
                ans[i] = '1'
                c = 1
            else:
                ans[i] = str(int(a[i]) + int(b[i]) + c)
                c = 0
        if c == 1:
            ans = ['1'] + ans
        return ''.join(ans)


a = '1111'
b = '1111'
Solution().addBinary(a, b)
