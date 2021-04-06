'''序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。

给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。

你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

示例 1:

输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
输出: true
示例 2:

输入: "1,#"
输出: false
示例 3:

输入: "9,#,#,1"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 槽位解法
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        treenode = preorder.split(',')
        slots = 1
        for i in treenode:
            if slots <= 0:
                return False
            if i == '#':
                slots -= 1
            else:
                slots += 1
        return slots == 0


# 不序列化的解法
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        prev = 1
        for i in preorder:
            if slots <= 0:
                return False
            if i == '#':
                slots -= 1
            elif i == ',':
                prev = 1
            elif prev:
                prev = 0
                slots += 1
        return slots == 0


a = "9,#,92,#,#"
Solution().isValidSerialization(a)
