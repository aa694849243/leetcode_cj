'''公司共有 n 个项目和  m 个小组，每个项目要不没有归属，要不就由其中的一个小组负责。

我们用 group[i] 代表第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于 -1。（项目和小组都是从零开始编号的）

请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：

同一小组的项目，排序后在列表中彼此相邻。
项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个项目左侧）应该完成的所有项目。
结果要求：

如果存在多个解决方案，只需要返回其中任意一个即可。

如果没有合适的解决方案，就请返回一个 空列表。

 

示例 1：



输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
输出：[6,3,4,1,5,2,0,7]
示例 2：

输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
输出：[]
解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。
 

提示：

1 <= m <= n <= 3*10^4
group.length == beforeItems.length == n
-1 <= group[i] <= m-1
0 <= beforeItems[i].length <= n-1
0 <= beforeItems[i][j] <= n-1
i != beforeItems[i][j]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_item = collections.defaultdict(set)
        group_indegree = collections.defaultdict(int)
        group_graph = collections.defaultdict(set)
        graph = collections.defaultdict(set)
        item_indegree = collections.defaultdict(int)
        zero_item = set()
        zero_group = set()
        sorted_group = []
        ans = []
        # 制作group和item的图
        for index, (g, pre) in enumerate(zip(group, beforeItems)):
            group_item[g].add(index)  # 将同一group的聚集到group_project中
            for pre_item in pre:
                graph[pre_item].add(index)  # item的图
                item_indegree[index] += 1  # item的入度
                if g != -1 and group[pre_item] != -1 and g != group[pre_item]:
                    group_graph[group[pre_item]].add(g)  # 绘制group_graph

        # 计算group的入度
        for g in group_graph:
            for dot in group_graph[g]:
                group_indegree[dot] += 1

        # 计算0度item
        for i in range(n):
            if item_indegree[i] == 0:
                zero_item.add(i)

        # 计算0度group
        for g in range(m):
            if group_indegree[g] == 0:
                zero_group.add(g)

        # 找出group的排序关系
        while zero_group:
            a = zero_group.pop()
            for g in group_graph[a]:
                group_indegree[g] -= 1
                if group_indegree[g] == 0:
                    zero_group.add(g)
            sorted_group.append(a)

        if len(sorted_group) != m:  # 如果sorted_group长度小于m说明存在回路，因为回路中的节点永远不可能进入0度表
            return []

        def update_item(item):
            '''更新item的后继节点和0度item表'''
            for i in graph[item]:
                item_indegree[i] -= 1
                if item_indegree[i] == 0:
                    zero_item.add(i)
            zero_item.remove(item)

        def process_init():
            '''处理初始条件，先将未分组的item和0度item表取交集'''
            while group_item[-1].intersection(zero_item):
                for item in group_item[-1].intersection(zero_item):
                    ans.append(item)
                    update_item(item)
                    group_item[-1].remove(item)

        # 依序处理sorted表中的group
        for current_group in sorted_group:
            process_init()  # 处理0度item表与group_item[-1]的交集
            while group_item[current_group].intersection(zero_item):  # 处理当前group与0度item表的交集
                for item in group_item[current_group].intersection(zero_item):
                    ans.append(item)
                    update_item(item)
                    group_item[current_group].remove(item)
        process_init()  # 最后再检查下group[-1]与0度item表是否有交集
        if len(ans) != n:  # 检查是否有环，有环的话将存在非0度item，则ans长度会小于n
            return []
        return ans


n = 8
m = 2
group = [-1, -1, 1, 0, 0, 1, 0, -1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Solution().sortItems(n=8, m=2, group=group,beforeItems=beforeItems)
