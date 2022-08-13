# 区间更新线段树，懒更新线段树
# 笔记
class segtree:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.treesum = 0
        self.mul = 1
        self.add = 0

    @property
    def _mid(self):
        return (self.l + self.r) // 2

    @property
    def _left(self):
        self.left = self.left or segtree(self.l, self._mid)
        return self.left

    @property
    def _right(self):
        self.right = self.right or segtree(self._mid + 1, self.r)
        return self.right

    def push_up(self):
        self.treesum = self._left.treesum + self._right.treesum
        self.treesum %= (10 ** 9 + 7)

    def add_update(self, ul, ur, val):
        if ul > ur:
            return
        if ul <= self.l and ur >= self.r:
            self.add += val
            self.treesum += (self.r - self.l + 1) * val
            self.treesum %= (10 ** 9 + 7)
            return
        self.lazy_push_down()
        if ul <= self._mid:
            self._left.add_update(ul, ur, val)
        if ur >= self._mid + 1:
            self._right.add_update(ul, ur, val)
        self.push_up()

    def mul_update(self, ul, ur, val):
        if ul > ur:
            return
        if ul <= self.l and ur >= self.r:
            self.mul *= val
            self.mul %= (10 ** 9 + 7)
            self.add *= val
            self.add %= (10 ** 9 + 7)
            self.treesum *= val
            self.treesum %= (10 ** 9 + 7)
            return
        self.lazy_push_down()
        if ul <= self._mid:
            self._left.mul_update(ul, ur, val)
        if ur >= self._mid + 1:
            self._right.mul_update(ul, ur, val)
        self.push_up()

    def query(self, ql, qr):
        if qr < self.l or ql > self.r:
            return 0
        if ql <= self.l and qr >= self.r:
            return self.treesum
        self.lazy_push_down()
        return (self._left.query(ql, qr) + self._right.query(ql, qr)) % (10 ** 9 + 7)

    def lazy_push_down(self):
        if self.add != 0 or self.mul != 1:
            self._left.treesum = (self._left.treesum * self.mul + self.add * (self._left.r - self._left.l + 1)) % (10 ** 9 + 7)
            self._right.treesum = (self._right.treesum * self.mul + self.add * (self._right.r - self._right.l + 1)) % (10 ** 9 + 7)
            self._left.mul *= self.mul
            self._right.mul *= self.mul
            self._left.add = self._left.add * self.mul + self.add
            self._right.add = self._right.add * self.mul + self.add
            self._left.mul %= (10 ** 9 + 7)
            self._left.add %= (10 ** 9 + 7)
            self._right.mul %= (10 ** 9 + 7)
            self._right.add %= (10 ** 9 + 7)
            self.add = 0
            self.mul = 1


class Fancy:

    def __init__(self):
        self.segtree = segtree(0, 10 ** 5)
        self.n = -1

    def append(self, val: int) -> None:
        self.n += 1
        self.segtree.add_update(self.n, self.n, val)

    def addAll(self, inc: int) -> None:
        if self.n >= 0:
            self.segtree.add_update(0, self.n, inc)

    def multAll(self, m: int) -> None:
        if self.n >= 0:
            self.segtree.mul_update(0, self.n, m)

    def getIndex(self, idx: int) -> int:
        if self.n < idx:
            return -1
        return self.segtree.query(idx, idx)


# Your Fancy object will be instantiated and called as such:
obj = Fancy()
obj.append(2)
obj.addAll(3)
obj.append(7)
obj.multAll(2)
print(obj.getIndex(0))
