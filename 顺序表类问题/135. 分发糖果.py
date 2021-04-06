'''
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:

输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2:

输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

# 暴力法
'''
最简单的方法是使用一个一维的数组 candiescandies 去记录给学生的糖果数。首先我们给每个学生 1 个糖果。然后我们开始从左到右扫描数组。对每一个学生，如果当前的评分 ratings[i]ratings[i] 比前一名学生的评分 ratings[i - 1]ratings[i−1] 高，且 candies[i]<=candies[i - 1]candies[i]<=candies[i−1] ，那么我们更新 candies[i] = candies[i-1] + 1candies[i]=candies[i−1]+1。这样，这两名学生之间的糖果分配目前是正确的。同样的，我们检查当前学生的评分 ratings[i]ratings[i] 是否比 ratings[i+1]ratings[i+1] 高，如果成立，我们同样更新 candies[i]=candies[i+1] + 1candies[i]=candies[i+1]+1 。我们继续对 ratingsratings 数组重复此步骤。如果在某次遍历中， candiescandies 数组不再变化，意味着我们已经得到了最后的糖果分布，此时可以停止遍历。为了记录是否到达最终状态，我们用 flagflag 记录每次遍历是否有糖果数目变化，如果有，则为 \text{True}True ，否则为 \text{False}False 。

最终，我们可以把 candiescandies 数组中所有糖果数目加起来，得到要求数目最少的糖果数。

作者：LeetCode
链接：https://leetcode-cn.com/problems/candy/solution/fen-fa-tang-guo-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


# 暴力法会超出时间限制
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) < 2:
            return len(ratings)
        candies = [1] * len(ratings)
        change = 1
        while change:
            change = 0
            for i in range(1, len(ratings)):
                if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                    candies[i] = candies[i - 1] + 1
                    change += 1
                elif ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                    candies[i - 1] = candies[i] + 1
                    change += 1
        return sum(candies)


'''
时间复杂度：O(n^2)。对于每个元素，我们最多要遍历 n 次。

空间复杂度： O(n) 。需要一个长度为 n 的 candies 数组。

作者：LeetCode
链接：https://leetcode-cn.com/problems/candy/solution/fen-fa-tang-guo-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


# 用两个数组
# 思路参照官方题解
class Solution:
    def candy(self, ratings: List[int]) -> int:
        lenth = len(ratings)
        if lenth < 2:
            return lenth
        left2right = [1] * lenth
        right2left = [1] * lenth
        for i in range(1, lenth):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1
        for i in range(lenth - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1
        candies = []
        for i in range(lenth):
            candies.append(max(left2right[i], right2left[i]))

        return sum(candies)


# 用一个数组
class Solution:
    def candy(self, ratings: List[int]) -> int:
        lenth = len(ratings)
        if lenth < 2:
            return lenth
        candies = [1] * lenth
        for i in range(1, lenth):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(lenth - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i + 1] + 1, candies[i])
        return sum(candies)


# 更巧妙的方法时间复杂度为O(n),空间复杂度为O(1),参考官方题解方法4

Solution().candy([1, 3, 2, 2, 1])
