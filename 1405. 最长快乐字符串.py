# -*- coding: utf-8 -*-
import heapq


# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
#
#  给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
#
#
#  s 是一个尽可能长的快乐字符串。
#  s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
#  s 中只含有 'a'、'b' 、'c' 三种字母。
#
#
#  如果不存在这样的字符串 s ，请返回一个空字符串 ""。
#
#
#
#  示例 1：
#
#  输入：a = 1, b = 1, c = 7
# 输出："ccaccbcc"
# 解释："ccbccacc" 也是一种正确答案。
#
#
#  示例 2：
#
#  输入：a = 2, b = 2, c = 1
# 输出："aabbc"
#
#
#  示例 3：
#
#  输入：a = 7, b = 1, c = 0
# 输出："aabaa"
# 解释：这是该测试用例的唯一正确答案。
#
#
#
#  提示：
#
#
#  0 <= a, b, c <= 100
#  a + b + c > 0
#
#  Related Topics 贪心 字符串 堆（优先队列）
#  👍 47 👎 0


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        li =[]
        for item in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if item[0]!=0:
                heapq.heappush(li,item)
        ans = ''
        cnt = 0
        while li:
            num, ch = heapq.heappop(li)
            if cnt == 2 and ch == ans[-1]:
                if not li:
                    break
                num_, ch_ = heapq.heappop(li)
                ans += ch_
                cnt = 1
                num_ += 1
                if num_<0:
                    heapq.heappush(li,(num_,ch_))
            else:
                num+=1
                if not ans or ch==ans[-1]:
                    cnt+=1
                else:
                    cnt=1
                ans+=ch
            if num<0:
                heapq.heappush(li,(num,ch))
        return ans
Solution().longestDiverseString(7,1,0)