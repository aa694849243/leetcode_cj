'''由 n 个连接的字符串 s 组成字符串 S，记作 S = [s,n]。例如，["abc",3]=“abcabcabc”。

如果我们可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。例如，根据定义，"abc" 可以从 “abdbec” 获得，但不能从 “acbbe” 获得。

现在给你两个非空字符串 s1 和 s2（每个最多 100 个字符长）和两个整数 0 ≤ n1 ≤ 106 和 1 ≤ n2 ≤ 106。现在考虑字符串 S1 和 S2，其中 S1=[s1,n1] 、S2=[s2,n2] 。

请你找出一个可以满足使[S2,M] 从 S1 获得的最大整数 M 。

 

示例：

输入：
s1 ="acb",n1 = 4
s2 ="ab",n2 = 2

返回：
2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-the-repetitions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# https://leetcode-cn.com/problems/count-the-repetitions/solution/tong-ji-zhong-fu-ge-shu-by-leetcode-solution/
# 循环节为什么一定存在 这里的鸽笼原理应该是说，每过一个s1，对应匹配到的s2的index只有|s2|种可能：0-|s2-1|，所以经过|s2|+1个s1，这个s1结束时匹配到的index必然和前面某个s1结束时匹配到的index相同。进一步，只要index“相同”就能找到循环节。
# 以下s1、s2表示小节，S1、S2表示全长字符串
# 例子 s1 ...ac..b|.ac..b|..ac.b|acb  s1中的acb本身就是1个循环节   acb acb acb acb acb acbacb acb
#     s2        b_ac|__b___ac|bac 下划线为空格            这里计算1个循环节有一个s2，相当于把后面的b补充到头部去了正好两个
#                      b 这个b补到前面去就是一个s2
# 例2

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        m = {}
        scn1 = 0  # s1个数
        scn2 = 0  # s2个数
        l2 = len(s2)
        s2index = 0
        while True:
            scn1 += 1  # 先拿出一个s1进行配对，假如第一个配到了需要的index，这个s1是不算进循环里的，后面的直到下一个index算一个循环节
            for ch in s1:
                if ch == s2[s2index]:
                    s2index += 1
                    if s2index == l2:
                        s2index = 0
                        scn2 += 1
            if scn1 >= n1:  # 没找到循环节，但是S1的字符串已经用完了，此时s2index未到s2尾部的话不能作数，即无法从S1里获得
                return scn2 // n2
            if s2index in m:  # 如果s2index存在记忆字典里，说明找到循环节
                scn1_prime, scn2_prime = m[s2index]
                scn1_loop, scn2_loop = scn1 - scn1_prime, scn2 - scn2_prime
                break
            else:
                m[s2index] = (scn1, scn2)
        ans = scn2_prime
        ans += (n1 - scn1_prime) // scn1_loop * scn2_loop
        rest = (n1 - scn1_prime) % scn1_loop #剩余的部分可以这样思考，首先把循环节部分配到头部,如我所写的例子中--这个b--，然后prime部分分为两部，前prime已经被scn1计算了，后prime部分相当于--这个b--也就是刚刚挪到前面代替的部分，然后根据循环匹配计算即可
        for i in range(rest):
            for ch in s1:
                if ch == s2[s2index]:
                    s2index += 1
                    if s2index == l2:
                        ans += 1
                        s2index = 1
        return ans//n2
Solution().getMaxRepetitions('acb',4,'bac',1)