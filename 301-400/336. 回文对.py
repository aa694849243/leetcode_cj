'''给定一组 互不相同 的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

 

示例 1：

输入：["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]]
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2：

输入：["bat","tab","cat"]
输出：[[0,1],[1,0]]
解释：可拼接成的回文串为 ["battab","tabbat"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 前缀树 字典树 manacher 马拉车
class trie:
    def __init__(self):
        self.lookup = {}

    def insert(self, word, j):
        tree = self.lookup
        if not word:  # 处理空字符
            tree['#'] = j
            return
        for i in word:
            if i not in tree:
                tree[i] = {}
            tree = tree[i]
        tree['#'] = j

    def search(self, word, j):
        tree = self.lookup
        if word != '#':
            for i in word:
                if i not in tree:
                    return -1
                tree = tree[i]
        c = tree.get('#')
        return c if c or c == 0 else -1


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def manacher(s):
            if len(s) < 2:
                return len(s)
            if len(s) == 2:
                return 2 if s[0] == s[1] else 1
            id = 0
            mx = 0
            sn = '#' + '#'.join(s) + '#'
            radius = [0] * len(sn)
            for i in range(len(radius)):
                if i < mx:
                    radius[i] = min(mx - i, radius[int(2 * id - i)])
                else:
                    radius[i] = 1
                while i - radius[i] >= 0 and i + radius[i] < len(radius) and sn[i - radius[i]] == sn[i + radius[i]]:
                    radius[i] += 1
                if i + radius[i] > mx:
                    mx, id = i + radius[i], i
            return max(radius) - 1

        tree_r = trie()
        for j in range(len(words)):  # 反向建立前缀树
            tree_r.insert(words[j][::-1], j)
        ans = []
        for j,word in enumerate(words):
            for i in range(len(word)+1):
                if manacher(word[i:]) == len(word) - i:  # 后缀是回文串，包括空字符串
                    b = tree_r.search(word[:i], j)  # 观察前缀是否在反向树中
                    if b != -1 and b != j:
                        ans.append([j, b])
                if i>0 and manacher(word[:i]) == i:  # 前缀是回文串，包括空字符串
                    a = tree_r.search(word[i:], j)  # 观察后缀是否在反向树中
                    if a != -1 and a != j:
                        ans.append([a, j])

        return ans

x = ['a','']
Solution().palindromePairs(x)
#哈希法
class Solution:
    def palindromePairs1(self, words: List[str]) -> List[List[int]]:

        # 核心思想--枚举前缀和后缀
        # 如果两个字符串k1，k2组成一个回文字符串会出现三种情况
        # len(k1) == len(k2),则需要比较k1 == k2[::-1]
        # len(k1) < len(k2),例如，k1=a, k2=abb,可组成abba
        #   因为k2后缀bb已经是回文字符串了，则需要找k1与k2剩下相等的部分
        # len(k1) > len(k2),例如，k1=bba, k2=a,组成abba
        #   因为k1前缀bb已经是回文字符串了，则需要找k1剩下与k2相等的部分

        res = []
        worddict = {word: i for i, word in enumerate(words)}  # 构建一个字典，key为word，valie为索引
        for i, word in enumerate(words):
            # i为word索引，word为字符串
            for j in range(len(word)+1):
                # 这里+1是因为，列表切片是前闭后开区间
                tmp1 = word[:j]  # 字符串的前缀
                tmp2 = word[j:]  # 字符串的后缀
                if tmp1[::-1] in worddict and worddict[tmp1[::-1]] != i and tmp2 == tmp2[::-1]:
                    # 当word的前缀在字典中，且不是word自身，且word剩下部分是回文(空也是回文)
                    # 则说明存在能与word组成回文的字符串
                    res.append([i, worddict[tmp1[::-1]]])  # 返回此时的word下标和找到的字符串下标

                if j > 0 and tmp2[::-1] in worddict and worddict[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:
                    # 当word的后缀在字典中，且不是word自身，且word剩下部分是回文(空也是回文)
                    # 则说明存在能与word组成回文的字符串
                    # 注意：因为是后缀，所以至少要从word的第二位算起，所以j>0
                    res.append([worddict[tmp2[::-1]], i])  # 返回此时的word下标和找到的字符串下标
        return res



x = ["abcd","dcba","lls","s","sssll"]
Solution().palindromePairs1(x)
