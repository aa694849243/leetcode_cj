'''
比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

你可以假设版本字符串非空，并且只包含数字和 . 字符。

 . 字符不代表小数点，而是用于分隔数字序列。

例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。

你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。
 

示例 1:

输入: version1 = "0.1", version2 = "1.1"
输出: -1
示例 2:

输入: version1 = "1.0.1", version2 = "1"
输出: 1
示例 3:

输入: version1 = "7.5.2.4", version2 = "7.5.3"
输出: -1
示例 4：

输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，“01” 和 “001” 表示相同的数字 “1”。
示例 5：

输入：version1 = "1.0", version2 = "1.0.0"
输出：0
解释：version1 没有第三级修订号，这意味着它的第三级修订号默认为 “0”。
 

提示：

版本字符串由以点 （.） 分隔的数字字符串组成。这个数字字符串可能有前导零。
版本字符串不以点开始或结束，并且其中不会有两个连续的点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compare-version-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def rec(v1, v2):
            if not v1 and not v2:
                return 0
            elif not v1:
                b = v2.index('.')
                if int(v2[:b]) > 0:
                    return -1
                elif int(v2[:b]) == 0:
                    return rec(v1, v2[b + 1:])
            elif not v2:
                a = v1.index('.')
                if int(v1[:a]) > 0:
                    return 1
                elif int(v1[:a]) == 0:
                    return rec(v1[a + 1:], v2)

            a = v1.index('.')
            b = v2.index('.')
            if int(v1[:a]) > int(v2[:b]):
                return 1
            elif int(v1[:a]) < int(v2[:b]):
                return -1
            else:
                return rec(v1[a + 1:], v2[b + 1:])

        return rec(version1+'.', version2+'.')


a = "1.0.1"
b = "1"
Solution().compareVersion(a,b)
