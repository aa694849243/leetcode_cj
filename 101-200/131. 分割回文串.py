'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        elif len(s)==1:
            return [[s]]
        res=[]
        def dfs(s,ans):
            if len(s)==0:
                res.append(ans)
            for i in range(1,len(s)+1):
                if s[:i]==s[i-1::-1]:
                    dfs(s[i:],ans+[s[:i]])
        dfs(s,[])
        return res

s="aab"
Solution().partition(s)