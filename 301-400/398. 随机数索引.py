'''给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

注意：
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

示例:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
solution.pick(3);

// pick(1) 应该返回 0。因为只有nums[0]等于1。
solution.pick(1);

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/random-pick-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# 数学
# 蓄水池问题
from typing import List
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums


    def pick(self, target: int) -> int:
        count=0
        res=-1
        for i in range(len(self.nums)):
            if self.nums[i]==target:
                if random.randint(0,count)==0: #判断如果等于目标值，依照概率保留res，比如有三个数，第一个数等于target，概率为1/2，第二个数来了，有1/2的概率丢弃第二个数，第三个数来了，有2/3的概率丢掉第三个数，依此类推，每次更新新的值概率为1/count
                    res=i
                count+=1
        return res







