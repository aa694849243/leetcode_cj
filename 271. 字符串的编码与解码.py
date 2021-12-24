# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 请你设计一个算法，可以将一个 字符串列表 编码成为一个 字符串。这个编码后的字符串是可以通过网络进行高效传送的，并且可以在接收端被解码回原来的字符串列表。
#
#
#  1 号机（发送方）有如下函数：
#
#  string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
#
#  2 号机（接收方）有如下函数：
#
#  vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
#
#
#  1 号机（发送方）执行：
#
#  string encoded_string = encode(strs);
#
#
#  2 号机（接收方）执行：
#
#  vector<string> strs2 = decode(encoded_string);
#
#
#  此时，2 号机（接收方）的 strs2 需要和 1 号机（发送方）的 strs 相同。
#
#  请你来实现这个 encode 和 decode 方法。
#
#  注意：
#
#
#  因为字符串可能会包含 256 个合法 ascii 字符中的任何字符，所以您的算法必须要能够处理任何可能会出现的字符。
#  请勿使用 “类成员”、“全局变量” 或 “静态变量” 来存储这些状态，您的编码和解码算法应该是非状态依赖的。
#  请不要依赖任何方法库，例如 eval 又或者是 serialize 之类的方法。本题的宗旨是需要您自己实现 “编码” 和 “解码” 算法。
#
#  Related Topics 设计 数组 字符串 👍 64 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ''
        for w in strs:
            ans += f'{len(w):4}'
            ans += w
        return ans

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        index = 0
        ans = []
        while index < len(s):
            leng = int(s[index:index + 4])
            index += 4
            ans.append(s[index:index + leng])
            index += leng
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# leetcode submit region end(Prohibit modification and deletion)
