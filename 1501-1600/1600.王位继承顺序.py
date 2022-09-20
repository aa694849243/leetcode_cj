from typing import List


# 多叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.childrens = []


# @solution-sync:begin
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.deaths = set()
        self.king = TreeNode(kingName)
        self.map = {kingName: self.king}

    def birth(self, parentName: str, childName: str) -> None:
        node = self.map[parentName]
        childnode = TreeNode(childName)
        node.childrens.append(childnode)
        self.map[childName] = childnode

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.res = []

        def dfs(node: TreeNode) -> None:
            if node.val not in self.deaths:
                self.res.append(node.val)
            if node.childrens:
                for child in node.childrens:
                    dfs(child)

        dfs(self.king)
        return self.res


# Your ThroneInheritance object will be instantiated and called as such:
obj = ThroneInheritance("king")
obj.birth("king", "andy")
obj.birth("king", "bob")
obj.birth("king", "catherine")
obj.birth("andy", "matthew")  # matthew is an indirect descendant of king.
# param_3 = obj.getInheritanceOrder()
