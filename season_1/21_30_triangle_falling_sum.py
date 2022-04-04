class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(1, len(triangle)):
            for c in range(0, len(triangle[r])):
                possibilities = []
                
                curval = triangle[r][c]
                
                if c > 0: 
                    possibilities.append(triangle[r-1][c-1] + curval)
                if c < len(triangle[r]) -1:
                    possibilities.append(triangle[r-1][c] + curval)
                
                triangle[r][c] = min(possibilities)
        
        return min(triangle[-1])