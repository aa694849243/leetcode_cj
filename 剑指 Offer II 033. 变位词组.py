# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-07 23:45 
# ide： PyCharm
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)
        for word in strs:
            tmp = [0] * 26
            for ch in word:
                tmp[ord(ch) - ord('a')] += 1
            m[tuple(tmp)].append(word)
        return list(m.values())

# leetcode submit region end(Prohibit modification and deletion)

