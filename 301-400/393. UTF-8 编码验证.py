'''UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：

对于 1 字节的字符，字节的第一位设为0，后面7位为这个符号的unicode码。
对于 n 字节的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为0，后面字节的前两位一律设为10。剩下的没有提及的二进制位，全部为这个符号的unicode码。
这是 UTF-8 编码的工作方式：

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
给定一个表示数据的整数数组，返回它是否为有效的 utf-8 编码。

注意:
输入是整数数组。只有每个整数的最低 8 个有效位用来存储数据。这意味着每个整数只表示 1 字节的数据。

示例 1:

data = [197, 130, 1], 表示 8 位的序列: 11000101 10000010 00000001.

返回 true 。
这是有效的 utf-8 编码，为一个2字节字符，跟着一个1字节字符。
示例 2:

data = [235, 140, 4], 表示 8 位的序列: 11101011 10001100 00000100.

返回 false 。
前 3 位都是 1 ，第 4 位为 0 表示它是一个3字节字符。
下一个字节是开头为 10 的延续字节，这是正确的。
但第二个延续字节不以 10 开头，所以是不符合规则的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/utf-8-validation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1 字符串方法
# format函数转换为2进制
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = 0
        for num in data:
            bin_num = format(num, '#010b')[-8:]  # 取二进制低8位
            if n == 0:
                for i in bin_num:
                    if i == '0':
                        break
                    n += 1
                if n == 0:  # 对于1byte字节，直接循环，避免-1
                    continue

                if n == 1 or n > 4:  # n代表前面1的个数,即总的字节数，如果n>4不符合要求，n==1代表只有一个字节，后续跟一个没有‘10’的字节，总共字节数就为2了，依旧不符合要求
                    return False
            else:
                if bin_num[0] != '1' and bin_num[1] != 0:
                    return False
            n -= 1
        return n == 0


# 2 位操作法
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        mask2 = 1 << 6
        n = 0
        for num in data:
            mask1 = 1 << 7
            if n == 0:
                while num & mask1:
                    mask1 >>= 1
                    n += 1
                if n == 0:
                    continue
                if n == 1 or n > 4:
                    return False
            else:
                if not (num & mask1 and not (num & mask2)):
                    return False
            n -= 1
        return n == 0


a = [197, 130, 1]
Solution().validUtf8(a)
