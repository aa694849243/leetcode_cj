'''二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。



例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

 

示例：

输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
 

提示：

输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
超过表示范围（小时 0-11，分钟 0-59）的数据将会被舍弃，也就是说不会出现 "13:00", "0:61" 等时间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-watch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []

        def hour(h, l, start):
            if h == 0:
                hl.append(l.copy())
                return
            for i in range(start, 4):
                l[i] = '1'
                hour(h - 1, l, i + 1)
                l[i] = '0'

        def minute(m, l, start):
            if m == 0:
                ml.append(l.copy())
                return
            for i in range(start, 6):
                l[i] = '1'
                minute(m - 1, l, i + 1)
                l[i] = '0'

        for i in range(5):
            if num - i >= 6 or num < i:
                continue
            hl = []
            ml = []
            hour(i, ['0', '0', '0', '0'], 0)
            minute(num - i, ['0', '0', '0', '0', '0', '0'], 0)
            for h in hl:
                for m in ml:
                    a = int(''.join(h), 2)
                    b = int(''.join(m), 2)
                    if a >= 12 or b>=60:
                        continue
                    a = str(a)
                    b = str(b) if b >= 10 else '0' + str(b)
                    res.append(a + ':' + b)
        return res


Solution().readBinaryWatch(1)
