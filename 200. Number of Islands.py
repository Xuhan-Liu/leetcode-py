from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def markLand(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0: return
            if grid[i][j] == "1":
                grid[i][j] = "2"
                markLand(i - 1, j)
                markLand(i + 1, j)
                markLand(i, j - 1)
                markLand(i, j + 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # print(i, j)
                    # print(grid)
                    markLand(i, j)
                    count += 1
        return count
