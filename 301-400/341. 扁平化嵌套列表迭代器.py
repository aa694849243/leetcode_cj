'''给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

 

示例 1:

输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
示例 2:

输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-nested-list-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # 对于nestedList中的内容，我们需要从左往右遍历，
        # 但堆栈pop是从右端开始，所以我们压栈的时候需要将nestedList反转再压栈
        self.stack = nestedList[::-1]

    def next(self) -> int:
        # hasNext 函数中已经保证栈顶是integer，所以直接返回pop结果
        return self.stack.pop(-1).getInteger()

    def hasNext(self) -> bool:
        # 对栈顶进行‘剥皮’，如果栈顶是List，把List反转再依次压栈，
        # 然后再看栈顶，依次循环直到栈顶为Integer。
        # 同时可以处理空的List，类似[[[]],[]]这种test case
        while len(self.stack) > 0 and self.stack[-1].isInteger() is False:
            self.stack += self.stack.pop().getList()[::-1]
        return len(self.stack) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())