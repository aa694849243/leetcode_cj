'''在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。

 

示例 :

输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
输出: True
解释:
我们可以通过以下几步将start转换成end:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
 

提示：

1 <= len(start) = len(end) <= 10000。
start和end中的字符串仅限于'L', 'R'和'X'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-adjacent-in-lr-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 1不可交换性 可到达性 ooperator
import operator


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False
        for symbol, op in (('L', operator.ge), ('R', operator.le)):
            mark = (i for i, x in enumerate(start) if x == symbol)
            for j, e in enumerate(end):
                if e == symbol and not op(next(mark), j):
                    return False
        return True


# 2双指针
import itertools


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        for (i, x), (j, y) in itertools.zip_longest(((i, x) for i, x in enumerate(start) if x != 'X'), ((j, y) for j, y in enumerate(end) if y != 'X'), fillvalue=(None, None)):
            if x != y or (x == 'R' and i > j) or (x == 'L' and i < j):
                return False
        return True


Solution().canTransform(start = "XXXL", end = "LXXL")
