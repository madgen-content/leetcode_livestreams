from typing import *
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        spec_coords = list()
        row_tracker = dict()
        col_tracker = dict()

        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                if v == 0:
                    continue

                if i not in row_tracker and j not in col_tracker:
                    row_tracker[i] = True
                    col_tracker[j] = True 
                    spec_coords.append((i,j))
                else:
                    row_tracker[i] = False
                    col_tracker[j] = False

        return sum(1 for i,j in spec_coords if row_tracker[i] and col_tracker[j])