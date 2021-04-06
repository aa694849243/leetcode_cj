'''打乱一个没有重复元素的数组。

 

示例:

// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shuffle-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_-1 = obj.reset()
# param_0 = obj.shuffle()
from typing import List

import random
class Solution:

    def __init__(self, nums: List[int]):
        self.org = nums.copy()
        self.arr = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.arr=self.org.copy()
        self.org=self.arr.copy()
        return self.arr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.arr)):
            swap_idx=random.randrange(i,len(self.arr))
            self.arr[i],self.arr[swap_idx]=self.arr[swap_idx],self.arr[i]
        return self.arr
n=[1,2,3,4]
a=Solution(n)
a.shuffle()


