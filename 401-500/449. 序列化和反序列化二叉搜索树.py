'''序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

编码的字符串应尽可能紧凑。

 

示例 1：

输入：root = [2,1,3]
输出：[2,1,3]
示例 2：

输入：root = []
输出：[]
 

提示：

树中节点数范围是 [0, 104]
0 <= Node.val <= 104
题目数据 保证 输入的树是一棵二叉搜索树。
 

注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1先后序遍历，后反转
# 注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []

        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        def hepler(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return
            val = data.pop()
            node = TreeNode(val)
            node.right = hepler(val, upper)  # 与后根序遍历方向完全相反
            node.left = hepler(lower, val)
            return node

        if not data:
            return
        data = [int(x) for x in data.split(' ')]
        return hepler()


# 2用4个字节表示整数 整数范围为[0,10^4]
# 不需要分割符

class Codec:
    def int_bit4(self, number):
        return ''.join([chr(number >> (8 * n) & 0xff) for n in range(4)])[::-1]

    def bit4_int(self, s):
        result = 0
        for ch in s:
            result = result * 256 + ord(ch)
        return result

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [self.int_bit4(root.val)] if root else []

        return ''.join(map(str, postorder(root)))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        def hepler(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return
            val = data.pop()
            node = TreeNode(val)
            node.right = hepler(val, upper)  # 与后根序遍历方向完全相反
            node.left = hepler(lower, val)
            return node

        if not data:
            return
        n = len(data)
        data = [self.bit4_int(data[i * 4:i * 4 + 4]) for i in range(n // 4)]
        return hepler()


a = TreeNode(None)
b = Codec().serialize(a)
