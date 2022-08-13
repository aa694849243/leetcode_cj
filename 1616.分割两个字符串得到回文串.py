class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if a == a[::-1] or b == b[::-1]:
            return True

        def judge(a, b):
            for i in range(size := len(a)):
                if i > size - i - 1:
                    return True
                if a[i] != b[size - i - 1]:
                    break
            else:
                return False
            return (b[i:size - i] != '' and b[i:size - i] == b[i:size - i][::-1]) or (a[i:-i] != '' and a[i:-i] == a[i:-i][::-1])

        return judge(a, b) or judge(b, a)


Solution().checkPalindromeFormation("xbdef", "xecab")
