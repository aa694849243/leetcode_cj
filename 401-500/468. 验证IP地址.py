'''编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。

如果是有效的 IPv4 地址，返回 "IPv4" ；
如果是有效的 IPv6 地址，返回 "IPv6" ；
如果不是上述类型的 IP 地址，返回 "Neither" 。
IPv4 地址由十进制数和点来表示，每个地址包含 4 个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1；

同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。

IPv6 地址由 8 组 16 进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。比如,  2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)。

然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。 比如， 2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。

同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如， 02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。

 

示例 1：

输入：IP = "172.16.254.1"
输出："IPv4"
解释：有效的 IPv4 地址，返回 "IPv4"
示例 2：

输入：IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
输出："IPv6"
解释：有效的 IPv6 地址，返回 "IPv6"
示例 3：

输入：IP = "256.256.256.256"
输出："Neither"
解释：既不是 IPv4 地址，又不是 IPv6 地址
示例 4：

输入：IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
输出："Neither"
示例 5：

输入：IP = "1e1.4.5.6"
输出："Neither"
 

提示：

IP 仅由英文字母，数字，字符 '.' 和 ':' 组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-ip-address
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 1正则表达式
# re.compile
import re


class Solution:
    def validIPAddress(self, IP: str) -> str:
        v4chunk = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        ipv4pattern = r'^(' + v4chunk + r'\.){3}' + v4chunk + r'$'
        v6chunk = r'[0-9a-fA-F]{1,4}'  # {}里用逗号
        ipv6pattern = r'^(' + v6chunk + r'\:){7}' + v6chunk + r'$'
        if '.' in IP:
            a = re.compile(ipv4pattern)
            return 'IPv4' if a.match(IP) else 'Neither'  # 有终止符号$不需要fullmatch
        elif ':' in IP:
            a = re.compile(ipv6pattern)
            return 'IPv6' if a.match(IP) else 'Neither'
        return 'Neither'


# 2分治法
class Solution:
    def validIPAddress(self, IP: str) -> str:
        def v4(IP):
            x = IP.split('.')
            if len(x) != 4:
                return 'Neither'
            for i in x:
                if len(i)==0 or (i[0] == '0' and len(i) > 1):
                    return 'Neither'
                elif not i.isdigit() or int(i) < 0 or int(i) > 255:
                    return 'Neither'
            return 'IPv4'

        def v6(IP):
            x = IP.split(':')
            if len(x) != 8:
                return 'Neither'
            m = '0123456789abcdefABCDEF'
            for s in x:
                if len(s) == 0 or len(s) > 4:
                    return 'Neither'
                for ch in s:
                    if ch not in m:
                        return 'Neither'
            return 'IPv6'
        if '.' in IP:
            return v4(IP)
        if ':' in IP:
            return v6(IP)
        return 'Neither'


Solution().validIPAddress("2001:db8:85a3:12:0:8A2E:0370:7334")
