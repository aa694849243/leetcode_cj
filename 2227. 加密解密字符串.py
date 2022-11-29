# -*- coding: utf-8 -*-
#  字符串 解密 按下述步骤进行：
#
#
#  将字符串每相邻 2 个字符划分为一个子字符串，对于每个子字符串 s ，找出满足 values[i] == s 的一个下标 i 。如果存在多个有效的 i ，
# 从中选择 任意 一个。这意味着一个字符串解密可能得到多个解密字符串。
#  在字符串中，用 keys[i] 替换 s 。
#
#
#  实现 Encrypter 类：
#
#
#  Encrypter(char[] keys, String[] values, String[] dictionary) 用 keys、values 和
# dictionary 初始化 Encrypter 类。
#  String encrypt(String word1) 按上述加密过程完成对 word1 的加密，并返回加密后的字符串。
#  int decrypt(String word2) 统计并返回可以由 word2 解密得到且出现在 dictionary 中的字符串数目。
#
#
#
#
#  示例：
#
#
# 输入：
# ["Encrypter", "encrypt", "decrypt"]
# [[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc",
# "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]
# 输出：
# [null, "eizfeiam", 2]
#
# 解释：
# Encrypter encrypter = new Encrypter([['a', 'b', 'c', 'd'], ["ei", "zf", "ei",
# "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]);
# encrypter.encrypt("abcd"); // 返回 "eizfeiam"。
#                            // 'a' 映射为 "ei"，'b' 映射为 "zf"，'c' 映射为 "ei"，'d' 映射为
# "am"。
# encrypter.decrypt("eizfeiam"); // return 2.
#                               // "ei" 可以映射为 'a' 或 'c'，"zf" 映射为 'b'，"am" 映射为
# 'd'。
#                               // 因此，解密后可以得到的字符串是 "abad"，"cbad"，"abcd" 和
# "cbcd"。
#                               // 其中 2 个字符串，"abad" 和 "abcd"，在 dictionary 中出现，所以
# 答案是 2 。
#
#
#
#
#  提示：
#
#
#  1 <= keys.length == values.length <= 26
#  values[i].length == 2
#  1 <= dictionary.length <= 100
#  1 <= dictionary[i].length <= 100
#  所有 keys[i] 和 dictionary[i] 互不相同
#  1 <= word1.length <= 2000
#  1 <= word2.length <= 200
#  所有 word1[i] 都出现在 keys 中
#  word2.length 是偶数
#  keys、values[i]、dictionary[i]、word1 和 word2 只含小写英文字母
#  至多调用 encrypt 和 decrypt 总计 200 次
#
#
#  Related Topics 设计 字典树 数组 哈希表 字符串
#  👍 19 👎 0
import collections

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keys = keys
        self.keys_m = {o: idx for idx, o in enumerate(keys)}
        self.values = values
        self.values_m = collections.defaultdict(set)
        for idx, word in enumerate(values):
            self.values_m[word].add(idx)
        self.dictionary = []
        for word in dictionary:
            if all([o in self.keys_m for o in word]):
                self.dictionary.append(word)

    def encrypt(self, word1: str) -> str:
        return ''.join(self.values[self.keys_m[c]] for c in word1)

    def decrypt(self, word2: str) -> int:
        lst = []
        cnt = 0
        for i in range(0, len(word2), 2):
            if word2[i:i + 2] not in self.values_m:
                return 0
            lst.append(self.values_m[word2[i:i + 2]])
        for word in self.dictionary:
            idx_lst = [self.keys_m[c] for c in word]
            if len(lst) != len(idx_lst):
                continue
            if all(idx in lst[i] for i, idx in enumerate(idx_lst)):
                cnt += 1
        return cnt


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
# leetcode submit region end(Prohibit modification and deletion)
keys, values, dictionary = [["b"], ["ca"], ["aaa", "cacbc", "bbaba", "bb"]]
word1 = "abcd"
word2 = "cacaca"
obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
print(obj.decrypt(word2))
