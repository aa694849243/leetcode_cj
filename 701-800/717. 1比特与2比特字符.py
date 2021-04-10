'''
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

示例 1:

输入:
bits = [1, 0, 0]
输出: True
解释:
唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
示例 2:

输入:
bits = [1, 1, 1, 0]
输出: False
解释:
唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
注意:

1 <= len(bits) <= 1000.
bits[i] 总是0 或 1.'''
from typing import List


# 1普通
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1] != 0:
            return False
        if len(bits) == 1:
            return True
        flag = True if bits[0] == 0 else False
        for i in range(1, len(bits)):
            if i == len(bits) - 1:
                return False if bits[i - 1] == 1 and flag == False else True
            if bits[i] == 0:
                flag = True
            elif bits[i] == 1:
                flag = not flag


# 2算最后一个0与前一个0的距离
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        a = 0
        bits.pop()
        while bits and bits.pop():
            a += 1

        return True if a % 2 == 0 else False


# 3算步数
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits)-1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return True if i==len(bits)-1 else False


Solution().isOneBitCharacter([1, 0, 0])
