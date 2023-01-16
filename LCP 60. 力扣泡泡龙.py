# -*- coding: utf-8 -*-
# 欢迎各位勇者来到力扣城，本次试炼主题为「力扣泡泡龙」。
#
# 游戏初始状态的泡泡形如二叉树 `root`，每个节点值对应了该泡泡的分值。勇者最多可以击破一个节点泡泡，要求满足：
# - 被击破的节点泡泡 **至多** 只有一个子节点泡泡
# - 当被击破的节点泡泡有子节点泡泡时，则子节点泡泡将取代被击破泡泡的位置
#
#  > 注：即整棵子树泡泡上移
#
# 请问在击破一个节点泡泡操作或无击破操作后，二叉泡泡树的最大「层和」是多少。
#
# **注意：**
# - 「层和」为同一高度的所有节点的分值之和
#
# **示例 1：**
#
# > 输入：`root = [6,0,3,null,8]`
# >
# > 输出：`11`
# >
# > 解释：勇者的最佳方案如图所示
# > ![image.png](https://pic.leetcode-cn.com/1648180809-XSWPLu-image.png){:
# height="100px"}
#
# **示例 2：**
#
# > 输入：`root = [5,6,2,4,null,null,1,3,5]`
# >
# > 输出：`9`
# >
# > 解释：勇者击破 6 节点，此时「层和」最大为 3+5+1 = 9
# > ![image.png](https://pic.leetcode-cn.com/1648180769-TLpYop-image.png){:
# height="200px"}
#
# **示例 3：**
#
# > 输入：`root = [-5,1,7]`
# >
# > 输出：`8`
# >
# > 解释：勇者不击破节点，「层和」最大为 1+7 = 8
#
# **提示**：
# - `2 <= 树中节点个数 <= 10^5`
# - `-10000 <= 树中节点的值 <= 10000`
#
#  Related Topics 树 动态规划 二叉树
#  👍 10 👎 0
from typing import List, Optional


# https://leetcode.cn/problems/WInSav/solution/by-newhar-7hps/
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMaxLayerSum(self, root: Optional[TreeNode]) -> int:
        level_infs = []
        remove_list = []

        def dfs(level, node):
            if not node:
                return 0
            while level + 1 >= len(level_infs):  # 保证level_infs长度至少比当前层多一层
                level_infs.append([[0, -1, -1, -1]])
            level_infs[level].append([
                level_infs[level][-1][0] + node.val,
                -1,
                len(level_infs[level + 1]),  # 记录当前节点左下位置
                -1])
            # node.val = len(level_infs[level]) - 1  # 修改节点的值为当前节点在当前层的位置
            if dfs(level + 1, node.left) + dfs(level + 1, node.right) != 2:  # 只有一个子节点
                remove_list.append([len(level_infs[level]) - 1,  # 记录当前节点在当前层的位置
                                    level])
            level_infs[level][-1][-1] = len(level_infs[level + 1]) - 1  # 修改当前节点的右下位置,当下一层空的时候right是会小于left的
            return 1

        visted = set()
        dfs(0, root)
        height = len(level_infs) - 1  # 最高的层数，-1是因为最后叶子节点加了一层
        res = float('-inf')
        for level in range(height):
            res = max(res, level_infs[level][-1][0])
        remove_list.sort(key=lambda x: x[1])  # 从上往下删，早删早得到大区间和
        for idx, (node, cur_level) in enumerate(remove_list):
            left = right = node
            lost = level_infs[cur_level][node][0] - level_infs[cur_level][node - 1][0]
            while cur_level < height:  # 最后一层不用考虑
                if right < left:
                    break
                if right - left + 1 == len(level_infs[cur_level]) - 1:  # left-right是当前层的所有节点，那么不用再往下遍历了，因为之后的变化量为0
                    break
                if (cur_level, left, right) in visted:
                    break
                visted.add((cur_level, left, right))
                nxt_level_presum, luse, nxt_level_left, _ = level_infs[cur_level][left]
                nxt_right_presum, ruse, _, nxt_level_right = level_infs[cur_level][right]
                # if luse != -1 and luse == ruse:  # 首先，不同父节点的子区间不会有交集。第二大区间永远强于小区间，已经考虑过大区间了，就不用再考虑小区间了
                #     break
                # luse = ruse = idx
                add = 0
                if nxt_level_left <= nxt_level_right:  # 说明下一层没有了,但是依旧可以比较下一层
                    add = level_infs[cur_level + 1][nxt_level_right][0] - level_infs[cur_level + 1][nxt_level_left - 1][0]
                res = max(res, level_infs[cur_level][-1][0] - lost + add)
                cur_level += 1
                lost = add
                left, right = nxt_level_left, nxt_level_right
        return res


# leetcode submit region end(Prohibit modification and deletion)
root = stringToTreeNode("[6,0,3,null,8]")
Solution().getMaxLayerSum(root)
