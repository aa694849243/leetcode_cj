'''给定两个字符串, A 和 B。

A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。

示例 1:
输入: A = 'abcde', B = 'cdeab'
输出: true

示例 2:
输入: A = 'abcde', B = 'abced'
输出: false
注意：

A 和 B 长度不超过 100。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A:
            return not B
        elif not B:
            return not A
        if len(A)!=len(B):
            return False
        flag=B[0]
        for i,ch in enumerate(A):
            if ch==flag:
                if A[i:]+A[:i]==B:
                    return True
        return False