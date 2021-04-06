'''一个强密码应满足以下所有条件：

由至少6个，至多20个字符组成。
至少包含一个小写字母，一个大写字母，和一个数字。
同一字符不能连续出现三次 (比如 "...aaa..." 是不允许的, 但是 "...aa...a..." 是可以的)。
编写函数 strongPasswordChecker(s)，s 代表输入字符串，如果 s 已经符合强密码条件，则返回0；否则返回要将 s 修改为满足强密码条件的字符串所需要进行修改的最小步数。

插入、删除、替换任一字符都算作一次修改。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/strong-password-checker
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 方法参考
# https://leetcode-cn.com/problems/strong-password-checker/solution/zhi-xing-1ms-ji-bai-100-javajie-ti-si-lu-by-chu-yu/
from typing import List


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        al, nu, Al = False, False, False
        m = {}
        if not password:
            return 6
        if password[0].isdigit():
            nu = True
        elif password[0].islower():
            al = True
        elif password[0].isupper():
            Al = True
        t = 1
        for i in range(1, n):
            if password[i].isdigit():
                nu = True
            elif password[i].islower():
                al = True
            elif password[i].isupper():
                Al = True
            if password[i] == password[i - 1]:
                t += 1
            else:
                if t >= 3:
                    m[i - 1] = t
                t = 1
        if t >= 3:
            m[i] = t
        if n < 6:
            return max(6 - n, 3 - (al + Al + nu))
        elif n <= 20:
            flag = 0
            for i in m:
                flag += m[i] // 3
            return max(3 - (al + Al + nu), flag)
        x = 3 - (al + Al + nu)  # x为缺失值
        m0, m1, m2 = {}, {}, {}
        ans = x  # x表示缺失数量，无论如何处理，至少需要转换x次
        for i in m:  # 分别处理不同余数的值，m2代表余数为2的字典，m1代表余数为1的字典，m0代表余数为0的字典
            if m[i] % 3 == 2:
                m2[i] = m[i]
            elif m[i] % 3 == 1:
                m1[i] = m[i]
            else:
                m0[i] = m[i]
        if x > 0:  # 先转换 %3==2的
            for i in m2:
                while m2[i] >= 3 and x > 0:  # 转换一次减少3个连续值
                    x -= 1
                    m2[i] -= 3
                if x == 0:
                    break
        if x > 0:  # 再转换 %3==1的
            for i in m1:
                while m1[i] >= 3 and x > 0:
                    x -= 1
                    m1[i] -= 3
                if x == 0:
                    break
        if x > 0:  # 最后转换 %3==0的
            for i in m0:
                while m0[i] >= 3 and x > 0:
                    x -= 1
                    m0[i] -= 3
                if x == 0:
                    break
        if x > 0:  # 转换完后x仍然大于0，说明连续的用光了，随便找一数转换为缺失数种类，再删掉多余的数即可，
            return ans + n - 20
        while m0 or m1 or m2:  # 缺失值补充完后仍有连续值，则先删 m0,再删m1,最后删m2
            k0 = list(m0.keys())
            for i in k0:
                a = m0.pop(i)  # 删掉i
                if a >= 3:
                    n -= 1
                    ans += 1
                    m2[i] = a - 1  # 余数变为2
                if n == 20:
                    break

            if n > 20:  # n>20说明删m0不够
                k1 = list(m1.keys())
                for i in k1:  # 再删m1
                    a = m1.pop(i)
                    if a >= 3:
                        n -= 2
                        ans += 2
                        m2[i] = a - 2  # 每次删2个，余数变为2
                    if n == 20:
                        break
                    if n == 19:  # 剩19个说明多删了，只需要删1个，省下连续的后面再处理
                        n += 1
                        ans -= 1
                        m0[i] = a - 1  # 删2个变为删1个
                        m2.pop(i)  # 删去刚刚增加的m2的值
                        break

            if n > 20:  # 删m1没结束
                k2 = list(m2.keys())
                for i in k2:  # 最后删m2
                    a = m2.pop(i)
                    if a >= 3:
                        n -= 3
                        ans += 3
                        m2[i] = a - 3
                    if n == 20:
                        break
                    elif n == 19:  # 假如剩下22个，删3个变为删2个
                        n += 1
                        ans -= 1
                        m0[i] = a - 2
                        m2.pop(i)
                        break
                    elif n == 18:  # 剩下21个，删3个变为删1个,留下%3==1的值
                        n += 2
                        ans -= 2
                        m1[i] = a - 1
                        m2.pop(i)
                        break
            if n <= 20:  # 删除到固定长度
                break
        if n > 20:  # 连续的用完了，删去多余的值即可
            return ans + n - 20
        for i in m2:  # 还有连续的，则检查连续值，依次替换得结果
            ans += m2[i] // 3
        for i in m1:
            ans += m1[i] // 3
        for i in m0:
            ans += m0[i] // 3
        return ans


Solution().strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc")
