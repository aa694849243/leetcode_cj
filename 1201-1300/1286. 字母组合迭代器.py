# -*- coding: utf-8 -*-
import itertools


# 请你设计一个迭代器类，包括以下内容：
#
#
#  一个构造函数，输入参数包括：一个 有序且字符唯一 的字符串 characters（该字符串只包含小写英文字母）和一个数字 combinationLengt
# h 。
#  函数 next() ，按 字典序 返回长度为 combinationLength 的下一个字母组合。
#  函数 hasNext() ，只有存在长度为 combinationLength 的下一个字母组合时，才返回 True；否则，返回 False。
#
#
#
#
#  示例：
#
#  CombinationIterator iterator = new CombinationIterator("abc", 2); // 创建迭代器 it
# erator
#
# iterator.next(); // 返回 "ab"
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 "ac"
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 "bc"
# iterator.hasNext(); // 返回 false
#
#
#
#
#  提示：
#
#
#  1 <= combinationLength <= characters.length <= 15
#  每组测试数据最多包含 10^4 次函数调用。
#  题目保证每次调用函数 next 时都存在下一个字母组合。
#
#  Related Topics 设计 回溯算法
#  👍 42 👎 0


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.li = list(itertools.combinations(characters, combinationLength))
        self.li.sort()
        self.p = 0
        self.n = len(self.li)
        self.leng = combinationLength

    def next(self) -> str:
        a = self.li[self.p]
        self.p+=1
        return ''.join(a)
    def hasNext(self) -> bool:
        if self.p>=self.n:
            return False
        return True

# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator('abc',2)
obj.next()
# param_2 = obj.hasNext()
