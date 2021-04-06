'''现有一个房间，墙上挂有 n 只已经打开的灯泡和 4 个按钮。在进行了 m 次未知操作后，你需要返回这 n 只灯泡可能有多少种不同的状态。

假设这 n 只灯泡被编号为 [1, 2, 3 ..., n]，这 4 个按钮的功能如下：

将所有灯泡的状态反转（即开变为关，关变为开）
将编号为偶数的灯泡的状态反转
将编号为奇数的灯泡的状态反转
将编号为 3k+1 的灯泡的状态反转（k = 0, 1, 2, ...)
示例 1:

输入: n = 1, m = 1.
输出: 2
说明: 状态为: [开], [关]
示例 2:

输入: n = 2, m = 1.
输出: 3
说明: 状态为: [开, 关], [关, 开], [关, 关]
示例 3:

输入: n = 3, m = 1.
输出: 4
说明: 状态为: [关, 开, 关], [开, 关, 开], [关, 关, 关], [关, 开, 开].
注意： n 和 m 都属于 [0, 1000].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bulb-switcher-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
import itertools


# https://leetcode-cn.com/problems/bulb-switcher-ii/solution/deng-pao-kai-guan-ii-by-leetcode/ 两颗赛艇的评论
class Solution:
    def flipLights(self, n: int, m: int) -> int:
        mem = set()
        for cand in itertools.product((0, 1), repeat=4):
            if sum(cand) % 2 == m % 2 and sum(cand) <= m:  # 操作数奇偶与总次数m相同且小于m
                a = []
                light = 1
                for i in range(min(3, n)):  # 只考虑前三个灯泡状态
                    light ^= cand[0]
                    light ^= cand[1] and i == 1  # 只有第二个灯才care第二个操作 或者用i%2==1
                    light ^= cand[2] and i % 2 == 0  # 第一个灯和第三个灯care第三个操作
                    light ^= cand[3] and i == 0  # 只有第一个灯care，或者用i%3==1
                    a.append(light)
                mem.add(tuple(a))
        return len(mem)
Solution().flipLights(1,1)