from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        origin = nums[:]
        nums.sort()
        if nums == origin:
            return 0
        start = 0
        end = 0
        for i in range(len(nums)):
            if nums[i] != origin[i]:
                start = i
                break
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != origin[i]:
                end = i
                break
        return end - start + 1
