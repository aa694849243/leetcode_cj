# 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
#
#
#  B.length >= 3
#  存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B
# [B.length - 1]
#
#
#  （注意：B 可以是 A 的任意子数组，包括整个数组 A。）
#
#  给出一个整数数组 A，返回最长 “山脉” 的长度。
#
#  如果不含有 “山脉” 则返回 0。
#
#
#
#  示例 1：
#
#  输入：[2,1,4,7,3,2,5]
# 输出：5
# 解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
#
#
#  示例 2：
#
#  输入：[2,2,2]
# 输出：0
# 解释：不含 “山脉”。
#
#
#
#
#  提示：
#
#
#  0 <= A.length <= 10000
#  0 <= A[i] <= 10000
#
#  Related Topics 双指针
#  👍 185 👎 0


from typing import List


# 1两个栈
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        ans = 0
        i = 0
        while i < len(arr) - 2:
            astack = [arr[i]]
            dstack = []
            for j in range(i + 1, len(arr)):
                if not dstack:
                    if arr[j] > astack[-1]:
                        astack.append(arr[j])
                    elif arr[j] == astack[-1] or arr[j] < astack[-1] and len(astack) == 1:
                        break
                    else:
                        dstack.append(arr[j])
                else:
                    if arr[j] >= dstack[-1]:
                        break
                    else:
                        dstack.append(arr[j])
            ans = max(ans, len(dstack) + len(astack)) if astack and dstack else ans
            i = j - 1 if j - 1 > i else i + 1
            if len(arr) - i <= ans:
                break
        return ans


# 2枚举山顶
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 0
        l, r = [0] * len(arr), [0] * len(arr)
        for i in range(1, len(arr)):
            l[i] = l[i - 1] + 1 if arr[i] > arr[i - 1] else 0
        for i in range(len(arr) - 2, -1, -1):
            r[i] = r[i + 1] + 1 if arr[i] > arr[i + 1] else 0
        ans=0
        for i in range(1,len(arr)-1):
            if l[i]>0 and r[i]>0:
                ans=max(ans,l[i]+r[i]+1)
        return ans
Solution().longestMountain([0,1,0])