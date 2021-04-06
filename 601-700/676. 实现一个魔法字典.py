'''设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。 如果给出一个单词，请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。

实现 MagicDictionary 类：

MagicDictionary() 初始化对象
void buildDict(String[] dictionary) 使用字符串数组 dictionary 设定该数据结构，dictionary 中的字符串互不相同
bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个 字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。
 

示例：

输入
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
输出
[null, null, false, true, false, false]

解释
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // 返回 False
magicDictionary.search("hhllo"); // 将第二个 'h' 替换为 'e' 可以匹配 "hello" ，所以返回 True
magicDictionary.search("hell"); // 返回 False
magicDictionary.search("leetcoded"); // 返回 False
 

提示：

1 <= dictionary.length <= 100
1 <= dictionary[i].length <= 100
dictionary[i] 仅由小写英文字母组成
dictionary 中的所有字符串 互不相同
1 <= searchWord.length <= 100
searchWord 仅由小写英文字母组成
buildDict 仅在 search 之前调用一次
最多调用 100 次 search

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-magic-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
from typing import List
import collections
import functools


# 1字典树
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        Trie = lambda: collections.defaultdict(Trie)
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        end = '#'
        for word in dictionary:
            functools.reduce(dict.__getitem__, word, self.trie)[end] = word

    def search(self, searchWord: str) -> bool:
        def dfs(word, flag, cur):
            if not word:  # word字符用完的情况
                if flag == 1 and '#' in cur:
                    return True
                else:
                    return False

            if word[0] not in cur and flag == 1:  # 发生不匹配，但之前已经替换过一次了
                return False
            else:
                for x in cur:  # 遍历所有可匹配字符，除了终点字符‘#’以外
                    if x != '#' and word[0] == x:  # word[0]匹配的情况
                        if flag == 0 and dfs(word[1:], 0, cur[x]):  # 之前没有替换的情况
                            return True
                        elif flag == 1 and dfs(word[1:], 1, cur[x]):  # 之前已经替换的情况
                            return True
                    elif x != '#' and word[0] != x and flag == 0 and dfs(word[1:], 1, cur[x]):  # 之前没有匹配过，则将这个word[0]设置为可匹配，flag置为1
                        return True
            return False

        return dfs(searchWord, 0, self.trie)


# 2广义邻居
import collections


class MagicDictionary:

    def _genneighbors(self, word):
        """
        Initialize your data structure here.
        """
        for i in range(len(word)):
            yield word[:i] + '*' + word[i + 1:]

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)
        self.m = collections.Counter(nei for word in self.words for nei in self._genneighbors(word))

    def search(self, searchWord: str) -> bool:
        return any(self.m[nei]>1 or self.m[nei]==1 and searchWord not in self.words for nei in self._genneighbors(searchWord))




obj = MagicDictionary()
obj.buildDict(["hello", "leetcode"])
obj.search("hell")
