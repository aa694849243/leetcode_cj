# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        c = Counter(words)
        length = len(words[0])
        ans = []
        for i in range(n * length - 1, len(s)):
            p = i - n * length + 1
            tmp = Counter()
            while p + length <= i + 1:
                if s[p:p + length] not in c or tmp[s[p:p + length]] == c[s[p:p + length]]:
                    break
                tmp[s[p:p + length]] += 1
                p += length
            if tmp == c:
                ans.append(i - n * length + 1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().findSubstring("a", ["a"])
)
