'''给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。

 

示例 1：

输入：
words = ["w","wo","wor","worl", "world"]
输出："world"
解释：
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
示例 2：

输入：
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出："apple"
解释：
"apply"和"apple"都能由词典中的单词组成。但是"apple"的字典序小于"apply"。
 

提示：

所有输入的字符串都只包含小写字母。
words数组长度范围为[1,1000]。
words[i]的长度范围为[1,30]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections
import functools


class Solution:
    def longestWord(self, words: List[str]) -> str:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        words.sort(key=lambda x: len(x))
        for word in words:
            functools.reduce(dict.__getitem__, word, trie)['#'] = '#'
        l = 0
        words = words[::-1]
        ans = 'z'*(len(words[0])+1)
        for word in words:
            t = trie
            for ch in word:
                if '#' in t[ch]:
                    t = t[ch]
                else:
                    break
            else:
                if len(word) < l:
                    break
                else:
                    ans = word if word < ans else ans
                    l=len(word)
        return ans if len(ans)<=len(words[0]) else ''
Solution().longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"])