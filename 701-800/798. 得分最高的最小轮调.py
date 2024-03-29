'''给定一个数组 A，我们可以将它按一个非负整数 K 进行轮调，这样可以使数组变为 A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。

例如，如果数组为 [2, 4, 1, 3, 0]，我们按 K = 2 进行轮调后，它将变成 [1, 3, 0, 2, 4]。这将记作 3 分，因为 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point]。

在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调索引 K。如果有多个答案，返回满足条件的最小的索引 K。

 

示例 1：

输入：[2, 3, 1, 4, 0]
输出：3
解释：
下面列出了每个 K 的得分：
K = 0,  A = [2,3,1,4,0],    score 2
K = 1,  A = [3,1,4,0,2],    score 3
K = 2,  A = [1,4,0,2,3],    score 3
K = 3,  A = [4,0,2,3,1],    score 4
K = 4,  A = [0,2,3,1,4],    score 3
所以我们应当选择 K = 3，得分最高。
示例 2：

输入：[1, 3, 0, 2, 4]
输出：0
解释：
A 无论怎么变化总是有 3 分。
所以我们将选择最小的 K，即 0。
 

提示：

A 的长度最大为 20000。
A[i] 的取值范围是 [0, A.length]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-rotation-with-highest-score
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1差分思想 轮调 区间覆盖
# 轮转次数做一个列表bad，bad的索引为轮转次数，值为不得分次数（取负值），遍历整个数组，每个数bad区间的位置全部减一，比如最后的结果为bad=[-1,-2,-2]，那么轮转次数为0为得分最大值，可以得2分，其他两个轮转都只能得1分，其他轮转次数总共只能得2分。为了线性时间操作，把bad改为差分序列，关于差分序列
# https://leetcode-cn.com/problems/smallest-rotation-with-highest-score/solution/de-fen-zui-gao-de-zui-xiao-lun-diao-by-leetcode/
class Solution:
    def bestRotation(self, A: List[int]) -> int:
        n = len(A)
        bad = [0] * n
        for i, x in enumerate(A):
            left, right = (i - x + 1) % n, (i + 1) % n  # 左闭右开
            bad[left] -= 1
            bad[right] += 1
            if left > right:  # left==right是不可能的，如果left>right需要补充个0处，而边界处对于差分序列是不动的
                bad[0] -= 1
        ans = 0
        best = -n
        cur = 0
        for i, score in enumerate(bad):
            if (cur := score + cur) > best:
                best = cur
                ans = i
        return ans


# 2懒惰传播+线段树,这个只能求区间最大值，无法求index是多少
import collections


# class Solution:
#     def __init__(self):
#         self.lazy = collections.defaultdict(int)
#         self.tree = collections.defaultdict(int)
#
#     def bestRotation(self, A: List[int]) -> int:
#         def update(s, e, l, r, id=0):
#             if r <= s or e <= l:
#                 return
#             if s <= l < r <= e:
#                 self.lazy[id] += 1
#                 self.tree[id] += 1
#             else:
#                 mid = (l + r) // 2
#                 update(s, e, l, mid, 2 * id + 1)
#                 update(s, e, mid, r, 2 * id + 2)
#                 self.tree[id] = self.lazy[id] + max(self.tree[2 * id + 1], self.tree[2 * id + 2])
#
#         for i, x in enumerate(A):  # good区间与bad区间互补
#             right = (i - x + 1) % len(A)
#             left = (i + 1) % len(A)
#             if left < right:
#                 update(left, right, 0, 20001, 0)
#             else:
#                 update(left, len(A), 0, 20001, 0)
#                 update(0, right, 0, 20001, 0)
#         return self.tree[0]


Solution().bestRotation([1, 3, 0, 2, 4])
