'''特殊的二进制序列是具有以下两个性质的二进制序列：

0 的数量与 1 的数量相等。
二进制序列的每一个前缀码中 1 的数量要大于等于 0 的数量。
给定一个特殊的二进制序列 S，以字符串形式表示。定义一个操作 为首先选择 S 的两个连续且非空的特殊的子串，然后将它们交换。（两个子串为连续的当且仅当第一个子串的最后一个字符恰好为第二个子串的第一个字符的前一个字符。)

在任意次数的操作之后，交换后的字符串按照字典序排列的最大的结果是什么？

示例 1:

输入: S = "11011000"
输出: "11100100"
解释:
将子串 "10" （在S[1]出现） 和 "1100" （在S[3]出现）进行交换。
这是在进行若干次操作后按字典序排列最大的结果。
说明:

S 的长度不超过 50。
S 保证为一个满足上述定义的特殊 的二进制序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/special-binary-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

import collections


class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        def rec(s):
            if len(s) == 2:
                return s
            n1, n0 = 0, 0
            flag = 0
            li = []
            l = 0
            for i, num in enumerate(s):
                if num == '1':
                    n1 += 1
                elif num == '0':
                    n0 += 1
                if i==len(s)-1 and l==0:
                    break
                if n1 == n0:
                    a = ''.join(rec(s[l:i + 1]))
                    li.append(a)
                    l = i + 1
                    flag = 1
            if not flag:
                return [s[0]] + rec(s[1:-1]) + [s[-1]]
            li.sort(reverse=True)
            return list(''.join(li))

        return ''.join(rec(list(S)))


Solution().makeLargestSpecial("11011000")
