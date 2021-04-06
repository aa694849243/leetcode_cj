'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

 

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

#回溯法 caojie 55
#时间复杂度不多于27次，3*3*3,第四次确定了
#空间复杂度不多于19,当字符串长度为8时，可能最多有19个解
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        res = []

        def dfs(s, j, ans):
            if len(s[j:]) < 4 - len(ans) or len(s[j:]) > 3 * (4 - len(ans)):
                return
            if len(ans) > 2:
                if int(s[j]) != 0 and int(s[j:]) <= 255:
                    res.append('.'.join(ans + [s[j:]]))
                elif int(s[j]) == 0 and len(s[j:]) == 1:
                    res.append('.'.join(ans + ['0']))
                else:
                    return
            else:
                for i in range(3):
                    if int(s[j]) != 0 and int(s[j:j + i + 1]) <= 255:
                        ans.append(s[j:j + i + 1])
                        dfs(s, j + i + 1, ans)
                        ans.pop()
                    elif int(s[j]) == 0 and i==0:
                        ans.append(s[j])
                        dfs(s, j + 1, ans)
                        ans.pop()
                    else:
                        return



        dfs(s, 0, [])
        return res


Solution().restoreIpAddresses("25525511135")
