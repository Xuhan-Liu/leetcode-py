from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # result = list(range(1, len(nums) + 1))
        # # result = [x for x in result if x not in nums]
        # n = len(nums)
        # for i in nums:
        return set(range(1, len(nums) + 1)).difference(set(nums))


        # return result
