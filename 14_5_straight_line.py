class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        diff_coords = [c for c in coordinates if c[0] != x0]
        if len(diff_coords) == 0:
            return True
        else:
            x1, y1 = diff_coords[0]

        slope = (y1-y0) / (x1-x0)

        b = y0 - slope * x0

        linechecker = lambda c: c[1] - slope * c[0] - b != 0 

        if any(map(linechecker,coordinates)):
            return False
        else:
            return True
        return