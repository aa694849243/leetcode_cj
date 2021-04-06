'''给定一个表示代码片段的字符串，你需要实现一个验证器来解析这段代码，并返回它是否合法。合法的代码片段需要遵守以下的所有规则：

代码必须被合法的闭合标签包围。否则，代码是无效的。
闭合标签（不一定合法）要严格符合格式：<TAG_NAME>TAG_CONTENT</TAG_NAME>。其中，<TAG_NAME>是起始标签，</TAG_NAME>是结束标签。起始和结束标签中的 TAG_NAME 应当相同。当且仅当 TAG_NAME 和 TAG_CONTENT 都是合法的，闭合标签才是合法的。
合法的 TAG_NAME 仅含有大写字母，长度在范围 [1,9] 之间。否则，该 TAG_NAME 是不合法的。
合法的 TAG_CONTENT 可以包含其他合法的闭合标签，cdata （请参考规则7）和任意字符（注意参考规则1）除了不匹配的<、不匹配的起始和结束标签、不匹配的或带有不合法 TAG_NAME 的闭合标签。否则，TAG_CONTENT 是不合法的。
一个起始标签，如果没有具有相同 TAG_NAME 的结束标签与之匹配，是不合法的。反之亦然。不过，你也需要考虑标签嵌套的问题。
一个<，如果你找不到一个后续的>与之匹配，是不合法的。并且当你找到一个<或</时，所有直到下一个>的前的字符，都应当被解析为 TAG_NAME（不一定合法）。
cdata 有如下格式：<![CDATA[CDATA_CONTENT]]>。CDATA_CONTENT 的范围被定义成 <![CDATA[ 和后续的第一个 ]]>之间的字符。
CDATA_CONTENT 可以包含任意字符。cdata 的功能是阻止验证器解析CDATA_CONTENT，所以即使其中有一些字符可以被解析为标签（无论合法还是不合法），也应该将它们视为常规字符。
合法代码的例子:

输入: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"

输出: True

解释:

代码被包含在了闭合的标签内： <DIV> 和 </DIV> 。

TAG_NAME 是合法的，TAG_CONTENT 包含了一些字符和 cdata 。

即使 CDATA_CONTENT 含有不匹配的起始标签和不合法的 TAG_NAME，它应该被视为普通的文本，而不是标签。

所以 TAG_CONTENT 是合法的，因此代码是合法的。最终返回True。


输入: "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"

输出: True

解释:

我们首先将代码分割为： start_tag|tag_content|end_tag 。

start_tag -> "<DIV>"

end_tag -> "</DIV>"

tag_content 也可被分割为： text1|cdata|text2 。

text1 -> ">>  ![cdata[]] "

cdata -> "<![CDATA[<div>]>]]>" ，其中 CDATA_CONTENT 为 "<div>]>"

text2 -> "]]>>]"


start_tag 不是 "<DIV>>>" 的原因参照规则 6 。
cdata 不是 "<![CDATA[<div>]>]]>]]>" 的原因参照规则 7 。
不合法代码的例子:

输入: "<A>  <B> </A>   </B>"
输出: False
解释: 不合法。如果 "<A>" 是闭合的，那么 "<B>" 一定是不匹配的，反之亦然。

输入: "<DIV>  div tag is not closed  <DIV>"
输出: False

输入: "<DIV>  unmatched <  </DIV>"
输出: False

输入: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
输出: False

输入: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
输出: False

输入: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
输出: False
注意:

为简明起见，你可以假设输入的代码（包括提到的任意字符）只包含数字, 字母, '<','>','/','!','[',']'和' '。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/tag-validator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 有限状态自动机

class Solution:
    def isValid(self, code: str) -> bool:
        if len(code) < 2:
            return False
        if code[0] != '<':
            return False
        state = 'start'
        states = {'start': ['start_tag_l'],
                  'start_tag_l': ['start_tag_l', 'tag_r'],
                  'tag_r': ['tag_r', 'start_tag_l', 'cdata_l', 'end_tag_l'],
                  'cdata_l': ['cdata_l', 'tag_r'],
                  'end_tag_l': ['end_tag_l', 'tag_r'],
                  }
        i = 0
        tag = ''
        stack = []
        while i < len(code):
            ch = code[i]
            if state == 'start':
                if ch == '<':
                    state = states[state][0]
                else:
                    return False
                i += 1
            elif state == 'start_tag_l':
                if ch.isupper():
                    tag += ch
                    state = states[state][0]
                elif ch == '>':
                    if 1 <= len(tag) <= 9:  # 标签长度要合法
                        state = states[state][1]
                        stack.append(tag)
                        tag = ''
                    else:
                        return False
                else:
                    return False
                i += 1
            elif state == 'tag_r':
                if ch == '<':
                    if i + 1 < len(code) and code[i + 1] != '!' and code[i + 1] != '/':
                        state = states[state][1]
                        i += 1
                    elif i + 1 < len(code) and code[i + 1] == '!':
                        if i + 8 < len(code) and code[i:i + 9] == "<![CDATA[":
                            state = states[state][2]
                            i += 9
                        else:
                            return False
                    elif i + 1 < len(code) and code[i + 1] == '/':
                        state = states[state][3]
                        i += 2
                    else:
                        return False
                else:
                    state = states[state][0]
                    i += 1
            elif state == 'cdata_l':
                if i + 2 < len(code) and code[i:i + 3] == ']]>':
                    state = states[state][1]
                    i += 3
                else:
                    state = states[state][0]
                    i += 1
            elif state == 'end_tag_l':
                if ch.isupper():
                    state = states[state][0]
                    tag += ch
                    i += 1
                elif ch == '>':
                    if stack:
                        tag_l = stack.pop()
                        if tag_l != tag:  # 一个闭合标签的匹配
                            return False
                        if not stack and i != len(code) - 1:  # 栈空了字符串还没有走完
                            return False
                        tag = ''
                        state = states[state][1]
                        i += 1
                    else:
                        return False
                else:
                    return False
        if stack or state != 'tag_r':
            return False
        return True


Solution().isValid("<A><A>")
