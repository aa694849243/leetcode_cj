'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def gen_pnext(p: str):
    k = -1
    pnext = [-1] * len(p)
    i = 0
    while i < len(p) - 1:
        if k == -1 or p[i] == p[k]:
            k += 1
            i += 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext


def strStr(haystack: str, needle: str) -> int:
    pnext = gen_pnext(needle)
    i, j = 0, 0
    n, m = len(haystack), len(needle)
    while i < n and j < m:
        if haystack[i] == needle[j] or j == -1:
            i += 1
            j += 1
        else:
            j = pnext[j]
    if j == m:
        return i - m
    else:
        return -1
