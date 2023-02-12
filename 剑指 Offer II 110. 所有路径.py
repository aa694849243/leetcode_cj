# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 21:13 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        def dfs(path):
            if path[-1]==len(graph)-1:
                res.append(path)
                return
            for i in graph[path[-1]]:
                dfs(path+[i])
        dfs([0])
        return res
# leetcode submit region end(Prohibit modification and deletion)

