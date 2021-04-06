'''有一个需要密码才能打开的保险箱。密码是 n 位数, 密码的每一位是 k 位序列 0, 1, ..., k-1 中的一个 。

你可以随意输入密码，保险箱会自动记住最后 n 位输入，如果匹配，则能够打开保险箱。

举个例子，假设密码是 "345"，你可以输入 "012345" 来打开它，只是你输入了 6 个字符.

请返回一个能打开保险箱的最短字符串。

 

示例1:

输入: n = 1, k = 2
输出: "01"
说明: "10"也可以打开保险箱。
 

示例2:

输入: n = 2, k = 2
输出: "00110"
说明: "01100", "10011", "11001" 也能打开保险箱。
 

提示：

n 的范围是 [1, 4]。
k 的范围是 [1, 10]。
k^n 最大可能为 4096。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cracking-the-safe
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# https://leetcode-cn.com/problems/cracking-the-safe/solution/po-jie-bao-xian-xiang-by-leetcode-solution/
# 欧拉回路 一笔画
# 将n-1位设置为node,每到1个node递归一下，保证不漏掉任何回路
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        seen = set()
        mod = 10 ** (n - 1)
        ans = []

        def dfs(num):
            for x in range(k):
                nei = num * 10 + x
                if nei not in seen:  # 序列已经在seen里了直接跳过
                    seen.add(nei)
                    dfs(nei % mod)  # 当序列已经为n位数了，则剥离首位数继续dfs
                    ans.append(str(x))  # 倒序输出节点值

        dfs(0)
        return ''.join(ans) + '0' * (n - 1) #因为答案是逆序输出的，假如开始节点是'000'+'X'，如果不补充0的话，这个方法会认为第一个数是'X'而不是'000X'


Solution().crackSafe(3, 2)
