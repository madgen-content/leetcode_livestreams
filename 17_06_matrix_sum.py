# coords are (row, col)
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if K == 0:
            return mat

        maxrow = len(mat)-1
        maxcol = len(mat[0]) -1 

        
        intermediate = [row[:] for row in mat]
        for row in intermediate:
            tot = 0
            for i in range(len(row)):
                val = row[i]
                tot += val
                row[i] = tot
        
        for i in range(maxrow + 1):
            for j in range(maxcol + 1):
                rightbound = min(j + K, maxcol)
                bottombound = min(i + K, maxrow)
                topbound = max(i - K, 0)
                leftbound = j - K - 1

                tot = 0
                for z in range(topbound, bottombound+1):
                    tot += intermediate[z][rightbound]
                
                if leftbound >= 0:
                    for z in range(topbound, bottombound+1):
                        tot -= intermediate[z][leftbound]
                
                mat[i][j] = tot

        return mat