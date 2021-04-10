'''给定一个包含 [0，n ) 中独特的整数的黑名单 B，写一个函数从 [ 0，n ) 中返回一个不在 B 中的随机整数。

对它进行优化使其尽量少调用系统方法 Math.random() 。

提示:

1 <= N <= 1000000000
0 <= B.length < min(100000, N)
[0, N) 不包含 N，详细参见 interval notation 。
示例 1:

输入:
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
输出: [null,0,0,0]
示例 2:

输入:
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
输出: [null,1,1,1]
示例 3:

输入:
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]
示例 4:

输入:
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
输出: [null,1,3,1]
输入语法说明：

输入是两个列表：调用成员函数名和调用的参数。Solution的构造函数有两个参数，N 和黑名单 B。pick 没有参数，输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/random-pick-with-blacklist
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

from typing import List
# 1随机类问题 黑名单映射
import random


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        blacklist.sort()
        x = N - len(blacklist)
        m = {}
        m2 = set(blacklist)
        for i in range(len(blacklist)):
            if blacklist[i] >= N - len(blacklist):
                break
            while x in m2:
                x += 1
            m[blacklist[i]] = x
            x += 1
        self.m = m
        self.N = N
        self.m2 = m2

    def pick(self) -> int:
        a = random.randint(0, self.N - len(self.m2) - 1)
        return self.m[a] if a in self.m else a


# 2二分法 特殊二分法
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.n = N - len(blacklist)
        self.li = sorted(blacklist)

    def pick(self) -> int:
        k = random.randint(0, self.n - 1)
        l, r = 0, len(self.li)
        if l == r:
            return k
        if self.li[0] >= k + 1:  # 黑名单最低位都高于目标值
            return k
        while l < r:
            mid = (l + r) // 2
            if self.li[mid] - mid < k + 1:  # 黑名单中间-中间==左侧白名单个数
                l = mid + 1
            else:
                r = mid

        if l >= len(self.li):  # 黑名单最后一位左侧白名单数数都小于目标值
            return k + l
            # self.li[l - 1] + (k + 1 - (self.li[l - 1] - (l - 1)))化简
        else:  # 黑名单[l]左侧白名单数都大于目标值,那么取l-1位左侧白名单数小于目标值，公式同上
            return k + l


# Your Solution object will be instantiated and called as such:
obj = Solution(5, [0, 1, 3])
obj.pick()
