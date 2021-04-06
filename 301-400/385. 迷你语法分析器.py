'''给定一个用字符串表示的整数的嵌套列表，实现一个解析它的语法分析器。

列表中的每个元素只可能是整数或整数嵌套列表

提示：你可以假定这些字符串都是格式良好的：

字符串非空
字符串不包含空格
字符串只包含数字0-9、[、-、,、]
 

示例 1：

给定 s = "324",

你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
示例 2：

给定 s = "[123,[456,[789]]]",

返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：

1. 一个 integer 包含值 123
2. 一个包含两个元素的嵌套列表：
    i.  一个 integer 包含值 456
    ii. 一个包含一个元素的嵌套列表
         a. 一个 integer 包含值 789

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/mini-parser
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


# NestedInteger(elem).add(NestedInteger(elem))=[NestedInteger,NestedInteger]处于同一层
# NestedInteger(elem).add(NestedInteger(NestedInteger(elem)))=[NestedInteger,[NestedInteger]] 有一个要高一层集
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()
        left = 0
        stack = []
        isnum = False
        for i in range(len(s)):
            if s[i] not in (',', '[', ']'):
                isnum = True
                continue
            elif s[i] == '[':
                stack.append(NestedInteger())
                left = i
            elif s[i] == ',' or s[i] == ']':
                if isnum:
                    num = int(s[left + 1:i])
                    cur_list = stack.pop()
                    cur_list.add(NestedInteger(num))
                    stack.append(cur_list)
                    isnum = False
                left = i
                if s[i] == ']' and len(stack) > 1:
                    cur_list = stack.pop()
                    stack[-1].add(cur_list)
        if isnum:
            stack.append(NestedInteger(int(s[:i + 1])))

        return stack[0]


a = "[123,456,[788,799,833],[[]],10,[]]"
b = "[123,[456,[788]]]"
Solution().deserialize(a)
