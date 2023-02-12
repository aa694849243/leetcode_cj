# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-07 23:08 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.f = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.f:
            return False
        self.f[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.f:
            return False
        r_idx = self.f[val]
        nr_idx = len(self.nums) - 1
        last_val = self.nums[nr_idx]
        self.f[last_val] = r_idx
        self.nums[r_idx], self.nums[nr_idx] = self.nums[nr_idx], self.nums[r_idx]
        self.nums.pop()
        del self.f[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)
