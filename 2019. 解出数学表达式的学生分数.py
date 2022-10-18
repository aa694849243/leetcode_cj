# -*- coding: utf-8 -*-
class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(l, r) -> set:
            if l == r:
                return {int(s[l])}
            tmp = set()
            for i in range(l, r + 1):
                if s[i] in '*+':
                    lset = dfs(l, i - 1)
                    rset = dfs(i + 1, r)
                    if s[i] == '*':
                        for a in lset:
                            for b in rset:
                                if a*b<=1000:
                                    tmp |= {a * b}
                    else:
                        for a in lset:
                            for b in rset:
                                if a+b<=1000:
                                    tmp |= {a + b}
            return tmp
        errors=dfs(0,len(s)-1)
        right = eval(s)
        c = collections.Counter(answers)
        res=0
        for num in c:
            if num == right:
                res+=5*c[num]
            elif num in errors:
                res+=2*c[num]
        return res
# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().scoreOfStudents("3+5*2",))