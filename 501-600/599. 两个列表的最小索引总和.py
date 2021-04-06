'''假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。

示例 1:

输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。
示例 2:

输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
输出: ["Shogun"]
解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
提示:

两个列表的长度范围都在 [1, 1000]内。
两个列表中的字符串的长度将在[1，30]的范围内。
下标从0开始，到列表的长度减1。
两个列表都没有重复的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1正常方法
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        milenth = len(list1) + len(list2)
        for i in range(len(list1)):
            if list1[i] in list2:
                if i + list2.index(list1[i]) < milenth:
                    res = [list1[i]]
                    milenth = i + list2.index(list1[i])
                elif i + list2.index(list1[i]) == milenth:
                    res.append(list1[i])
        return res


# 按列表长度和遍历
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lenth = len(list1) + len(list2) - 2
        res = []
        flag = 0
        for i in range(lenth + 1):
            for j in range(min(i + 1, len(list1))):
                k = i - j
                if k < len(list2) and list1[j] == list2[k]:
                    res.append(list1[j])
                    flag = 1
            if flag:
                break
        return res


Solution().findRestaurant(["vacag", "KFC"], ["fvo", "xrljq", "jrl", "KFC"])
