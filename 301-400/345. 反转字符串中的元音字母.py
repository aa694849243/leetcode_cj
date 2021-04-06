'''编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

 

示例 1：

输入："hello"
输出："holle"
示例 2：

输入："leetcode"
输出："leotcede"
 

提示：

元音字母不包含字母 "y" 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        m = {'a', 'e', 'i', 'o', 'u'}
        ans = [''] * len(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left] not in m:
                ans[left] = s[left]
                left += 1
            while left < right and s[right] not in m:
                ans[right] = s[right]
                right -= 1
            if left < right and s[left] in m and s[right] in m:
                ans[left], ans[right] = s[right], s[left]
                left += 1;
                right -= 1
        if left==right:
            ans[right]=s[right]
        return ''.join(ans)


Solution().reverseVowels('fowo')
