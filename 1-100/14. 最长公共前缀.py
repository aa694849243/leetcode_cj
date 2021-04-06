'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# -------------------------caojie---9.45%-------------------------------------------------------------------------
def longestCommonPrefix(strs: list) -> str:
    if len(strs) == 0:
        return ''
    # if len(strs) == 1:
    #     return strs[0] 这两段不需要
    s = strs[0]
    for i in range(1, len(strs)):  # 从第二个之后比
        j = 0
        ans = ''
        while j < min(len(s), len(strs[i])):
            if s[j] == strs[i][j]:  # 比对字符，相同的留下
                ans += s[j]
                j += 1
            else:
                break
        s = ans  # 更新公共前缀s
    return s
#-----------------------------------zip函数解法---------------------------------------------------------------------------
def longestCommonPrefix(self, strs: List[str]) -> str:
    s = ""
    for i in zip(*strs):
        if len(set(i)) == 1:
            s += i[0]
        else:
            break
    return s



strs = ["flower", "flow", "flight"]
list(zip(*strs))
longestCommonPrefix(strs)
