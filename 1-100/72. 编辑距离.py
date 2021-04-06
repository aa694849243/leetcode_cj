'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1) + len(word2)
        n1, n2 = len(word1), len(word2)
        mem = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        mem[0] = [i for i in range(n2 + 1)]
        for i in range(n1 + 1):
            mem[i][0] = i
        for j in range(1, n2 + 1):
            for i in range(1, n1 + 1):
                if word1[i - 1] == word2[j - 1]:
                    mem[i][j] = min(mem[i][j - 1], mem[i - 1][j], mem[i - 1][j - 1] - 1) + 1
                else:
                    mem[i][j] = min(mem[i][j - 1], mem[i - 1][j], mem[i - 1][j - 1]) + 1
        return mem[i][j]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1) + len(word2)
        n1, n2 = len(word1), len(word2)
        mem = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        mem[0] = [i for i in range(n2 + 1)]
        for i in range(n1 + 1):
            mem[i][0] = i
        for j in range(1, n2 + 1):
            for i in range(1, n1 + 1):
                if word1[i - 1] == word2[j - 1]:
                    mem[i][j] = mem[i - 1][j - 1]
                else:
                    mem[i][j] = min(mem[i][j - 1], mem[i - 1][j], mem[i - 1][j - 1]) + 1
        return mem[i][j]


word1 = "horse"
word2 = "ros"
Solution().minDistance(word1, word2)
