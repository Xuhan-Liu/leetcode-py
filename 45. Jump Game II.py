from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n, cnt, furthest, end = len(nums), 0, 0, 0
        for i in range(n - 1):
            furthest = max(furthest, nums[i] + i)
            if i == end:
                cnt += 1
                end = furthest

        return cnt
