'''给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。

换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。

注意，删除一个元素后，子数组 不能为空。

请看示例：

示例 1：

输入：arr = [1,-2,0,3]
输出：4
解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。
示例 2：

输入：arr = [1,-2,-2,3]
输出：3
解释：我们直接选出 [3]，这就是最大和。
示例 3：

输入：arr = [-1,-1,-1,-1]
输出：-1
解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
     我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。
 

提示：

1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray-sum-with-one-deletion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
# f[i]以arr[i]结尾的删除0个数的子数组最大和
# f1[i]以arr[i]结尾的删除1个数的子数组最大和
# 那么转移方程：
#     f[i] = max(arr[i], f[i-1]+arr[i])     要么从当前数开始，要么从前一个数开始
#     f1[i] = arr[i] + max(f1[i-1], f[i-2]) 要么删除arr[i-1]之前的任意数, 要么删除arr[i-1]
#
# 作者：lin-500
# 链接：https://leetcode-cn.com/problems/maximum-subarray-sum-with-one-deletion/solution/yi-tang-bian-li-dpsuan-fa-by-lin-500/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
import collections


# 动态规划+前缀和
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if not arr:
            return 0
        if len(arr) < 2:
            return arr[0]

        f = [0] * len(arr)  # 以i结尾不删任何值
        f1 = [0] * len(arr)  # 以i结尾删 1个值
        f[0], f[1] = arr[0], max(arr[0] + arr[1], arr[1])
        f1[0], f1[1] = 0, arr[1]  # 这里初始化的f1[x]略有不同，f1[0]表示的是删掉第一个的值，f1[2]会自然比对删除第一个和第二个的最大值
        ans = max(f[0], f[1], f1[1])
        for i in range(2,len(arr)):
            f[i] = max(arr[i], f[i - 1] + arr[i])
            f1[i] = arr[i] + max(f[i - 2], f1[i - 1])  # 可能会存在最后一个arr[i]删掉无法考虑，但删掉arr[i]相当于前i-1个数相加==f[i-1]
            ans = max(f[i], f1[i], ans)
        return ans


Solution().maximumSum([1,-2,0,3])
