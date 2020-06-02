'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 回溯法--------------------------------------------遇到0时回溯-----------------------------------------------------------
def letterCombinations(digits: str) -> list:
    if len(digits) == 0:
        return []
    t = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = []

    def backtrack(combination, nextdigit):  # combination表示前一步的序列，nextdigit表示接下来字符串第一个数字所代表的字母候选，全部可能都要加上
        if len(nextdigit) == 0:  # 当序列到达最后一步，则将所有组成的combin加入列表中
            res.append(combination)
        else:
            for letter in t[nextdigit[0]]:
                backtrack(combination + letter, nextdigit[1:])

    backtrack('', digits)
    return res


# -----------多重列表推导式-------------------------------------------------------------------------------------------
def letterCombinations(digits: str) -> list:
    conversion = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits) == 0:
        return []
    product = ['']
    for k in digits:
        product = [i + j for i in product for j in conversion[k]] #列表推导式多重for，每一步都更新product，每一不都需要从更新的produt中取i值
    return product


digits = '23'
letterCombinations(digits)
