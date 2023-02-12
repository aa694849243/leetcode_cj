# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-09 23:32 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.f = {}
        self.m = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.m:
            new_val = val - self.m[key]
            self.m[key] = val
            val=new_val
        else:
            self.m[key] = val
        tree = self.f
        for c in key:
            if c not in tree:
                tree[c] = [{}, 0]
            tree[c][1] += val
            tree = tree[c][0]

    def sum(self, prefix: str) -> int:
        tree = self.f
        ans = 0
        for c in prefix:
            if c not in tree:
                return 0
            ans = tree[c][1]
            tree = tree[c][0]
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# leetcode submit region end(Prohibit modification and deletion)
obj = MapSum()
obj.insert("apple", 3)
obj.insert("apple", 2)
obj.insert("apple", 1)
print(obj.sum("ap"))

