# 有一个特殊的正方形房间，每面墙上都有一面镜子。除西南角以外，每个角落都放有一个接受器，编号为 0， 1，以及 2。
#
#  正方形房间的墙壁长度为 p，一束激光从西南角射出，首先会与东墙相遇，入射点到接收器 0 的距离为 q 。
#
#  返回光线最先遇到的接收器的编号（保证光线最终会遇到一个接收器）。
#
#
#
#  示例：
#
#
# 输入： p = 2, q = 1
# 输出： 2
# 解释： 这条光线在第一次被反射回左边的墙时就遇到了接收器 2 。
#
#
#
#
#  提示：
#
#
#  1 <= p <= 1000
#  0 <= q <= p
#
#  Related Topics 数学
#  👍 52 👎 0

# 1数学法
# qt=np   qt/n=p

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def gcd(p, q):
            if q == 0:
                return p
            else:
                return gcd(q, p % q)

        k = gcd(p, q)
        lcm = p * q // k
        t = lcm // q  # t为时间步
        if t % 2 and (lcm // p) % 2:
            return 1
        elif t % 2 and not (lcm % p) % 2:
            return 0
        else:
            return 2


# 2模拟法
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        from fractions import Fraction
        target = {(p, 0), (p, p), (0, p)}
        x, y = 0, 0
        vx, vy = p, q
        while (x, y) not in target:
            t = float('inf')
            for v in [Fraction(-x, vx), Fraction(-y, vy), Fraction(p - x, vx), Fraction(p - y, vy)]:  # 计算时间
                if v > 0: t = min(t, v)  # 找到最早触摸墙的时间，记录下来
            x += vx * t
            y += vy * t
            if x == p or x==0: vx *= -1
            if y == p or y==0: vy *= -1
        if vx<0 and vy<0: return 1 #原方向都为正，反射后为负数，则到达0点
        elif vx<0 and vy>0: return 0
        else: return 2



Solution().mirrorReflection(p=2, q=1)
