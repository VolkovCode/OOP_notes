
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
         
        return nums

S = Solution()
nums = [1,2,3,4,5,6,7, 1]
k = 3
print(id(nums))
nums.remove(1)
print(id(nums))
print(S.rotate(nums, k))
