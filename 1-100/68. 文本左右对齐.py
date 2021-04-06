'''
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/text-justification
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        ans = []
        while i < len(words):
            s = []
            lenth = 0
            count = 0
            while lenth <= maxWidth + 1 and i < len(words):  # 取出1行
                s.append(words[i])
                lenth += (len(words[i]) + 1)
                count += 1
                i += 1
            if lenth > maxWidth + 1:  # 如果是因为长度超出了，则弹出最后一个加进去的
                lenth = lenth - (len(s.pop()) + 1)
                i -= 1
                count -= 1
            else:  # 如果是到了最后一个，直接pass
                pass
            spax = maxWidth + 1 - lenth  # 需要额外补括号的长度
            n = spax // (count - 1) if count > 1 else spax  # 平均每两个词间需要多+n个括号
            reminder = spax % (count - 1) if count > 1 else 0  # 冗余的长度
            st = ''
            if count == 1:  # 一行只有一个词的情况
                ans.append(s[0] + spax * ' ')
            elif i != len(words):  # 非最后一行的情况
                for m in s[:-1]:
                    st = st + m + ' ' + ' ' * n + " " if reminder > 0 else st + m + ' ' + ' ' * n
                    reminder -= 1
                st += s[-1]
                ans.append(st)
            else:  # 最后一行的情况
                for m in s:
                    st = st + m + ' '
                spax = maxWidth - len(st)
                st = st + ' ' * spax if spax >= 0 else st[:-1]
                ans.append(st)
        return ans


words = ["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do", "for",
         "your", "country"]
maxWidth = 16
Solution().fullJustify(words, maxWidth)
