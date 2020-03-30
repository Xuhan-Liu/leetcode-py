from typing import List


class Solution:
    def __init__(self):
        self.grid = None
        self.col = 0
        self.row = 0

    def affectOthers(self, i, j):
        if i + 1 < self.row and self.grid[i + 1][j] == 1:
            self.grid[i + 1][j] = 2
        if j + 1 < self.col and self.grid[i][j + 1] == 1:
            self.grid[i][j + 1] = 2
        if i - 1 >= 0 and self.grid[i - 1][j] == 1:
            self.grid[i - 1][j] = 2
        if j - 1 >= 0 and self.grid[i][j - 1] == 1:
            self.grid[i][j - 1] = 2

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])

        minutes = 0
        left_fresh = 0
        while True:
            left_fresh = 0
            past_grid = [x[:] for x in self.grid]
            for i in range(self.row):
                for j in range(self.col):
                    if past_grid[i][j] == 2:
                        self.affectOthers(i, j)
                    if self.grid[i][j] == 1:
                        left_fresh += 1
            if past_grid == self.grid and left_fresh > 0:
                return -1
            if past_grid == self.grid:
                return minutes
            minutes += 1
