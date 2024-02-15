from typing import List

from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mem = [[[None for _ in range(n)] for _ in range(n)] for _ in range(m)]
        return self.cherryPick(grid, 0, 0, n - 1, mem)
    
    def cherryPick(self, grid: List[List[int]], x: int, y1: int, y2: int, mem: List[List[List[int]]]) -> int:
        if x == len(grid):
            return 0
        if y1 < 0 or y1 == len(grid[0]) or y2 < 0 or y2 == len(grid[0]):
            return 0
        if mem[x][y1][y2] is not None:
            return mem[x][y1][y2]
        
        currRow = grid[x][y1] + (0 if y1 == y2 else 1) * grid[x][y2]
        
        max_cherries = 0
        for d1 in [-1, 0, 1]:
            for d2 in [-1, 0, 1]:
                max_cherries = max(max_cherries, currRow + self.cherryPick(grid, x + 1, y1 + d1, y2 + d2, mem))
        
        mem[x][y1][y2] = max_cherries
        return max_cherries

ints = Solution()
grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
res = ints.cherryPickup(grid)

print(res)

    
