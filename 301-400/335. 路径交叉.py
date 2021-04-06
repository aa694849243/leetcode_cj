'''给定一个含有 n 个正数的数组 x。从点 (0,0) 开始，先向北移动 x[0] 米，然后向西移动 x[1] 米，向南移动 x[2] 米，向东移动 x[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。

编写一个 O(1) 空间复杂度的一趟扫描算法，判断你所经过的路径是否相交。

 

示例 1:

┌───┐
│   │
└───┼──>
    │

输入: [2,1,1,2]
输出: true
示例 2:

┌──────┐
│      │
│
│
└────────────>

输入: [1,2,3,4]
输出: false
示例 3:

┌───┐
│   │
└───┼>

输入: [1,1,1,1]
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/self-crossing
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        def four(x):
            if x[-1] >= x[-3] and x[-4] >= x[-2]:
                return True
            else:
                return False

        def five(x):
            if x[-1] >= x[-3] and x[-4] > x[-2]:
                return True
            elif x[-4] == x[-2] and x[-5] + x[-1] >= x[-3]:
                return True
            else:
                return False
        def six(x):
            if x[-3] > x[-5] and x[-2] < x[-4] and x[-1] + x[-5] >= x[-3] and x[-2] + x[-6] >= x[-4]:
                return True
            elif x[-2] == x[-4] and x[-1] + x[-5] >= x[-3]:
                return True
            else:
                return False


        if len(x) < 4:
            return False
        elif len(x) == 4:
            return four(x)
        elif len(x) == 5:
            if four(x[:4]) or five(x):
                return True
            else:
                return False
        elif len(x) >= 6:
            if four(x[:4]) or five(x[:5]) or six(x[:6]):
                return True
            else:
                for i in range(7,len(x)+1):
                    if six(x[i-6:i]):
                        return True
                return False


Solution().isSelfCrossing([2, 1, 1, 2, 5, 8, 2, 3])
