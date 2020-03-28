from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        self.sum = 0

        def markLand(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0: return
            if grid[i][j] == 1:
                grid[i][j] = 2
                self.sum += 1
                markLand(i - 1, j)
                markLand(i + 1, j)
                markLand(i, j - 1)
                markLand(i, j + 1)

        maxArea = self.sum
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    markLand(i, j)
                    maxArea = max(maxArea, self.sum)
                    self.sum = 0
        return maxArea
