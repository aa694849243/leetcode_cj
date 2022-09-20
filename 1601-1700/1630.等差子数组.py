from typing import List


# @solution-sync:begin
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def judge(lst):
            if len(lst) < 3:
                return True
            nlst = sorted(lst)
            d = nlst[1] - nlst[0]
            for i in range(2, len(nlst)):
                if nlst[i] - nlst[i - 1] != d:
                    return False
            return True
        res=[]
        for l_,r_ in zip(l,r):
            res.append(judge(nums[l_:r_+1]))
        return res
