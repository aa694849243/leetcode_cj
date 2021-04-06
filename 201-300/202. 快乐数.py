'''
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

 

示例：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


#分析看官方题解
#数学
# 哈希表法 哈希法
class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while n != 1 and n not in hashset:
            hashset.add(n)
            x = 0
            while n:
                x += (n % 10) ** 2
                n //= 10
            n = x
        return True if n == 1 else False


# 快慢指针

class Solution:
    def isHappy(self, n: int) -> bool:
        def getnext(n):
            x = 0
            while n:
                x += (n % 10) ** 2
                n //= 10
            return x

        a, b = getnext(n), getnext(getnext(n))
        while a != b and b != 1:
            a = getnext(a)
            b = getnext(getnext(b))
        return True if b==1 else False

#规律
def isHappy(self, n: int) -> bool:

    cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    while n != 1 and n not in cycle_members:
        n = get_next(n)

    return n == 1

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/happy-number/solution/kuai-le-shu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
a = 19
Solution().isHappy(a)
