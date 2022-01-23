'''假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。

在每一步操作中，你可以选择任意 m （1 ≤ m ≤ n） 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。

给定一个非负整数数组代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的最少的操作步数。如果不能使每台洗衣机中衣物的数量相等，则返回 -1。

 

示例 1：

输入: [1,0,5]

输出: 3

解释:
第一步:    1     0 <-- 5    =>    1     1     4
第二步:    1 <-- 1 <-- 4    =>    2     1     3
第三步:    2     1 <-- 3    =>    2     2     2
示例 2：

输入: [0,3,0]

输出: 2

解释:
第一步:    0 <-- 3     0    =>    1     2     0
第二步:    1     2 --> 0    =>    1     1     1
示例 3:

输入: [0,2,0]

输出: -1

解释:
不可能让所有三个洗衣机同时剩下相同数量的衣物。
 

提示：

n 的范围是 [1, 10000]。
在每台超级洗衣机中，衣物数量的范围是 [0, 1e5]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-washing-machines
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

# 假设对于前 i 台洗衣机，总共多了y件衣服，需要传递y次将多余的衣服转移出来，那么对于i+1处，假如其少了x件衣服，它达到目标值需要max(x,y)次，此时前i+1的前缀和一定小于y的；假如多了x件衣服，那么i+1处达到目标值需要y+x(等于前i+1的前缀和)次，因此每一步的最少的操作步数为“数组元素的最大值”和“数组元素前缀和的绝对值的最大值”中的较大值
import itertools


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        if sum(machines) % len(machines):
            return -1
        target = sum(machines) // len(machines)
        a = []
        for i in range(len(machines)):
            a.append(machines[i] - target)
        b = [*itertools.accumulate(a)]
        d = map(abs, b)
        return max(max(a), max(d))


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        dress_total = sum(machines)
        if dress_total % n != 0:
            return -1

        dress_per_machine = dress_total // n
        for i in range(n):
            # Change the number of dresses in the machines to
            # the number of dresses to be removed from this machine
            # (could be negative)
            machines[i] -= dress_per_machine

        # curr_sum is a number of dresses to move at this point,
        # max_sum is a max number of dresses to move at this point or before,
        # m is number of dresses to move out from the current machine.
        curr_sum = max_sum = res = 0
        for m in machines:
            curr_sum += m
            max_sum = max(max_sum, abs(curr_sum))
            res = max(res, max_sum, m)
        return res

Solution().findMinMoves([9,1,8,8,9])
