from typing import List


# solution one
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         nums.sort()
#         for i in range(len(nums)):
#             if i != nums[i]:
#                 return i
#         return len(nums)

# solution two
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = int(n * (n + 1) / 2)
        return _sum - sum(nums)
