'''给定一个排序好的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：

|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b
 

示例 1：

输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]
示例 2：

输入：arr = [1,2,3,4,5], k = 4, x = -1
输出：[1,2,3,4]
 

提示：

1 <= k <= arr.length
1 <= arr.length <= 104
数组里的每个元素与 x 的绝对值不超过 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-k-closest-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1排序
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        a = []
        for i, num in enumerate(arr):
            a.append([abs(x - num), num])
        a.sort()
        ans = []
        for i in range(k):
            ans.append(a[i][1])
        ans.sort()
        return ans


# 2二分 双指针
import bisect


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = bisect.bisect_left(arr, x)
        l, r = ind - 1, ind
        ans = []
        while len(ans) < k:
            if r >= len(arr) or l >= 0 and abs(x - arr[l]) <= abs(x - arr[r]):
                ans.append(arr[l])
                l -= 1
            elif l < 0 or r < len(arr) and abs(x - arr[l]) > abs(x - arr[r]):
                ans.append(arr[r])
                r += 1
        return sorted(ans)
arr=[-2,-1,1,2,3,4,5]
k=7
x=3
Solution().findClosestElements(arr,k,x)