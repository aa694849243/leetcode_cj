import functools


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @functools.lru_cache(None)
        def f(ch, i):
            if i == 0:
                return 1
            ans = 0
            ans += f('u', i - 1)
            if ch == 'u':
                return ans
            ans += f('o', i - 1)
            if ch == 'o':
                return ans
            ans += f('i', i - 1)
            if ch == 'i':
                return ans
            ans += f('e', i - 1)
            if ch == 'e':
                return ans
            ans += f('a', i - 1)
            return ans
        return f('a',n-1)+f('e',n-1)+f('i',n-1)+f('o',n-1)+f('u',n-1)
