from typing import *

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                possibles = []
                
                if i == 0 and j==0:
                    grid[0][0] = (v,v)
                    continue
                
                if i > 0:
                    possibles.extend(grid[i-1][j])
                
                if j > 0:
                    possibles.extend(grid[i][j-1])
                
                hi = max(possibles)
                lo = min(possibles)

                grid[i][j] = (v*lo, v*hi)
        
        ret = max(grid[-1][-1])
        return ret % 1000000007 if ret >= 0 else -1