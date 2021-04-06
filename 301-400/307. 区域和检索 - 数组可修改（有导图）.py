'''给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。

示例:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
说明:

数组仅可以在 update 函数下进行修改。
你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-mutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.a = []
        x = 0
        for i in range(len(nums)):
            x += nums[i]
            self.a.append(x)

    def update(self, i: int, val: int) -> None:
        y = val - self.nums[i]
        for j in range(i, len(self.a)):
            self.a[j] += y
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        if not i:
            return self.a[j]
        return self.a[j] - self.a[i - 1]


# sqrt分块法
class NumArray:

    def __init__(self, nums: List[int]):
        self.lenth = len(nums)
        self.nums = nums
        self.bl = int(self.lenth ** 0.5)
        self.block = []
        a = 0
        for i in range(self.lenth):
            if not i or i % self.bl:
                a += nums[i]
            else:
                self.block.append(a)
                a = nums[i]
        self.block.append(a)

    def update(self, i: int, val: int) -> None:
        x = i // self.bl
        self.block[x] += (val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        a = i // self.bl
        b = j // self.bl
        ans = 0
        for k in range(a, b):
            ans += self.block[k]
        for m in range(a * self.bl, i):
            ans -= self.nums[m]
        for n in range(b * self.bl, j + 1):
            ans += self.nums[n]
        return ans


# 线段树

class Segment_tree:

    def __init__(self, nums: List[int], merge):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * 4 * self.n  # 树里面存储子节点的和，两倍应该够了
        self.merge = merge
        if self.n:
            self.build(0, 0, self.n - 1)

    def build(self, treeindex, l, r):
        if l == r:
            self.tree[treeindex] = self.nums[l]
            return
        mid = (l + r) // 2
        left, right = 2 * treeindex + 1, 2 * treeindex + 2  # left,right为左右节点在树中的坐标
        self.build(left, l, mid)
        self.build(right, mid + 1, r)
        self.tree[treeindex] = self.merge(self.tree[left], self.tree[right])

    def update(self, dataindex, val):
        self.nums[dataindex] = val
        self._update(0, dataindex, 0, self.n - 1)

    def _update(self, treeindex, dataindex, l, r):
        if l == r == dataindex:
            self.tree[treeindex] = self.nums[dataindex]
            return
        mid = (l + r) // 2
        left, right = 2 * treeindex + 1, 2 * treeindex + 2
        if dataindex <= mid:
            self._update(left, dataindex, l, mid)
        else:
            self._update(right, dataindex, mid + 1, r)
        self.tree[treeindex] = self.merge(self.tree[left], self.tree[right])

    def quary(self, l, r):
        return self._quary(0, 0, self.n - 1, l, r)

    def _quary(self, treeindex, left, right, l, r):
        if l == left and r == right:  # 这里的left,right指的是数组的左右边界
            return self.tree[treeindex]
        mid = (left + right) // 2
        tree_left, tree_right = 2 * treeindex + 1, 2 * treeindex + 2
        if r <= mid:
            return self._quary(tree_left, left, mid, l, r)
        elif l > mid:
            return self._quary(tree_right, mid + 1, right, l, r)
        return self.merge(self._quary(tree_left, left, mid, l, mid), self._quary(tree_right, mid + 1, right, mid + 1, r))


class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = Segment_tree(nums, lambda x, y: x + y)

    def update(self, i: int, val: int) -> None:
        self.tree.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.tree.quary(i, j)


# ["NumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
# [[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]]
c = NumArray([0, 9, 5, 7, 3])
c.sumRange(4, 4)
c.sumRange(2, 4)
c.sumRange(0, 2)
