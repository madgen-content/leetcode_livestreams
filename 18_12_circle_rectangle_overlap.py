def dist_squared(p1,p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return dx * dx + dy * dy

def vertical_boundary_distance(center, low_point, high_point):
    
    if center[1] < low_point[1]:
        return dist_squared(center, low_point)
    elif center[1] > high_point[1]:
        return dist_squared(center, high_point)
    else:
        dx = center[0] - low_point[0]
        return dx * dx
    return

def horizontal_boundary_distance(center, left_point, right_point):
    
    if center[0] < left_point[0]:
        return dist_squared(center, left_point)
    elif center[0] > right_point[0]:
        return dist_squared(center, right_point)
    else:
        dy = center[1] - left_point[1]
        return dy * dy
    return

class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        # do simple check for center inside of bounds
        if x_center >= x1 and x_center <= x2 and y_center >= y1 and y_center <= y2:
            return True
        
        if radius == 0:
            return False

        rsq = radius * radius

        center = (x_center, y_center)
        bl = (x1, y1)
        tr = (x2, y2)
        tl = (x1, y2)
        br = (x2, y1)

        dists = []
        dists.append(vertical_boundary_distance(center, bl, tl))
        dists.append(vertical_boundary_distance(center, br, tr))
        dists.append(horizontal_boundary_distance(center, tl, tr))
        dists.append(horizontal_boundary_distance(center, bl, br))

        if min(dists) <= rsq:
            return True

        
        return False