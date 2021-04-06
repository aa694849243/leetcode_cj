'''
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

 

示例 1：

输入："/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。
示例 2：

输入："/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
示例 3：

输入："/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
示例 4：

输入："/a/./b/../../c/"
输出："/c"
示例 5：

输入："/a/../../b/../c//.//"
输出："/c"
示例 6：

输入："/a//b////c/d//././/.."
输出："/a/b/c"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/simplify-path
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# caojie-----------11%
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ''
        ans = []
        stock = []
        count = 0
        for i in range(len(path)):
            if path[i] == '/':
                if not ans:
                    ans.append('/')
                elif ans[-1] != '/':
                    ans.append(path[i])
                elif count != 0:
                    if count == 1:
                        stock.pop()
                        count = 0
                    elif count == 2:
                        if len(ans) > 1:
                            ans.pop()
                            while ans[-1] != '/':
                                ans.pop()
                        stock.pop()
                        stock.pop()
                        count = 0
                    else:
                        ans.extend(stock)
                        stock.clear()
                        count = 0
            elif path[i] == '.':
                if ans and ans[-1] == '/' and count == 0:
                    stock.append('.')
                    count = 1
                elif stock:
                    stock.append('.')
                    count += 1
            else:
                stock.append(path[i])
                ans.extend(stock)
                stock.clear()
                count = 0
        if count == 2:
            if len(ans) > 1:
                ans.pop()
                while ans[-1] != '/':
                    ans.pop()
        elif count > 2:
            ans.extend(stock)
        res = ''.join(ans)
        return res[:-1] if res[-1] == '/' and len(res) != 1 else res


# 利用split做栈
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for item in path:
            if item == "..":
                if stack: stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)


# 作者：powcai
# 链接：https://leetcode-cn.com/problems/simplify-path/solution/zhan-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 利用字典解题
class Solution:
    def simplifyPath(self, path: str) -> str:
        r = []
        for s in path.split('/'):
            r = {'': r, '.': r, '..': r[:-1]}.get(s, r + [s])
        return '/' + '/'.join(r)


# 作者：QQqun902025048
# 链接：https://leetcode-cn.com/problems/simplify-path/solution/python-4-line-by-qqqun902025048/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution().simplifyPath("/home/")
