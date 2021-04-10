'''这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8。

arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？

示例 1:

输入: arr = [5,4,3,2,1]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。
示例 2:

输入: arr = [2,1,3,4,4]
输出: 4
解释:
我们可以把它分成两块，例如 [2, 1], [3, 4, 4]。
然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。
注意:

arr的长度在[1, 2000]之间。
arr[i]的大小在[0, 10**8]之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-chunks-to-make-sorted-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections


# 1排序计数 caojie
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        arr2 = sorted(arr)
        m1, m2 = collections.defaultdict(int), collections.defaultdict(int)
        ans = 0
        for i in range(len(arr)):
            m1[arr[i]] += 1
            m2[arr2[i]] += 1
            if m1 == m2:
                ans += 1
                m1, m2 = collections.defaultdict(int), collections.defaultdict(int)
        return ans


class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.Counter()
        counted = []
        for x in arr:
            count[x] += 1
            counted.append((x, count[x]))

        ans, cur = 0, None
        for X, Y in zip(counted, sorted(counted)):
            cur = max(cur, X)
            if cur == Y:
                ans += 1
        return ans


# 2官方仿写 双指针
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        m = collections.defaultdict(int)
        arr2 = sorted(arr)
        ans, nonezero = 0, 0
        for i in range(len(arr)):
            m[arr[i]] += 1
            if m[arr[i]] == 1:
                nonezero += 1
            elif m[arr[i]] == 0:
                nonezero -= 1
            m[arr2[i]] -= 1
            if m[arr2[i]] == 0:
                nonezero -= 1
            elif m[arr2[i]] == -1:
                nonezero += 1
            if nonezero == 0:
                ans += 1
        return ans


# 3官方仿写 排序计数
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        m = collections.Counter()
        count = []
        for i in range(len(arr)):
            m[arr[i]] += 1
            count.append((arr[i], m[arr[i]]))
        ans, cur = 0,(-1,-1)
        for X, Y in zip(count, sorted(count)):
            cur=max(X,cur)
            if cur==Y:
                ans+=1
        return ans
Solution().maxChunksToSorted([2, 1, 3, 4, 4])
