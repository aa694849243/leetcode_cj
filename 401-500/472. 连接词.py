# 给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。
#
#  连接词 定义为：一个完全由给定数组中的至少两个较短单词（不一定是不同的两个单词）组成的字符串。
#
#
#
#  示例 1：
#
#
# 输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses",
# "rat","ratcatdogcat"]
# 输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
# 解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成;
#      "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成;
#      "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
#
#
#  示例 2：
#
#
# 输入：words = ["cat","dog","catdog"]
# 输出：["catdog"]
#
#
#
#  提示：
#
#
#  1 <= words.length <= 10⁴
#  1 <= words[i].length <= 30
#  words[i] 仅由小写英文字母组成。
#  words 中的所有字符串都是 唯一 的。
#  1 <= sum(words[i].length) <= 10⁵
#
#
#  Related Topics 深度优先搜索 字典树 数组 字符串 动态规划
#  👍 298 👎 0
import functools


# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    def __init__(self):
        self.lookup = {}

    def insert(self, word):
        node = self.lookup
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = '#'

    def search(self, word):
        node = self.lookup
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node
    def dfs(self,word,pos,visted):
        if not word or pos>=len(word):
            return True
        if visted[pos]:
            return False
        visted[pos] = True
        for i in range(pos,len(visted)):
            if self.search(word[pos:i+1]) and self.dfs(word,i+1,visted):
                return True
        return False


from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        trie = Trie()
        res = []
        for word in words:
            if trie.dfs(word,0,[False]*len(word)):
                res.append(word)
            else:
                trie.insert(word)
        return res
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().findAllConcatenatedWordsInADict(
["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
))