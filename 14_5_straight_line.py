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

# alternative courtesy of zombiekillerwhale
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        p1, p2 = coordinates[0], coordinates[1]
        x_diff = p2[0] - p1[0]
        y_diff = p2[1] - p1[1]
        try:
            m = y_diff / x_diff
        except ZeroDivisionError:
            return all(coordinate[0] == p1[0] for coordinate in coordinates)
        b = -(m * p1[0]) + p1[1]
        return all(m * x + b == y for x, y in coordinates)