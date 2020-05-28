"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

'--------------------------------caojie---哈希表法---------------------------------------------------------'


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '哈希表法'
        d = {}
        start = 0  # 起点位置，相当于左窗口
        max_lenth = 0  # 最大长度
        for i, l in enumerate(s):
            if l in d:  # 如果碰到之前存在的字符，更新起点，即更新左窗口
                start = d[l] + 1 if d[l] + 1 > start else start
            lenth_ = i - start + 1  # i相当于右窗口，长度等于右窗减去左窗
            max_lenth = lenth_ if lenth_ > max_lenth else max_lenth
            d[l] = i  # 将列表中的值存入字典，索引对应值，列表中的值对应键
        return max_lenth


'-------------滑动窗口法--------------------------------------------------------------------------------------'


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 如果字符串s为空，返回0
        if not s: return 0
        # 保存窗口内字符串
        lookup = list()
        n = len(s)
        # 最大子串长度
        max_len = 0
        # 当前窗口长度
        cur_len = 0
        # 遍历字符串s
        for i in range(n):
            val = s[i]
            # 如果该值不在窗口中
            if not val in lookup:
                # 添加到窗口内
                lookup.append(val)
                # 当前长度+1
                cur_len += 1
            # 如果该值在窗口中已存在
            else:
                # 获取其在窗口中的位置
                index = lookup.index(val)
                # 移除该位置及之前的字符，相当于上图中的图3到图4
                lookup = lookup[index + 1:]
                lookup.append(val)
                # 当前长度更新为窗口长度
                cur_len = len(lookup)
            # 如果当前长度大于最大长度，更新最大长度值
            if cur_len > max_len: max_len = cur_len
        # 返回最大子串长度
        return max_len


'''作者：superychen
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-tu-wen-jiang-jie-by-superychen/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
