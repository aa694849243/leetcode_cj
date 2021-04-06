'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]  # 初始化，长度+1
        dp[0] = True  # 0号位为True
        for i in range(0, len(s)):
            for j in range(i + 1):
                if s[j:i + 1] in wordDict and dp[j]:  # 找断点，和断点前是否为True
                    dp[i + 1] = True
                    break
        return dp[-1]


# 动态规划---
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = [True, s[0] in wordDict]
#         for i in range(1, len(s)):
#             for j in range(i + 1):
#                 if s[j: i + 1] in wordDict and dp[j]:
#                     dp.append(True)
#                     break
#             else:
#                 dp.append(False)
#         return dp[-1]


s = "catsandog"
wordDict = ["cats", "dog", 'sand', 'and', 'cat', 'og']
Solution().wordBreak('a', ['a'])
# 作者：ting-ting-28
# 链接：https://leetcode-cn.com/problems/word-break/solution/python3-dong-tai-gui-hua-by-ting-ting-28-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
