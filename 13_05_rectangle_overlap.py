class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec2[1] < rec1[3] and rec2[3] > rec1[1] and rec2[0] < rec1[2] and rec2[2] > rec1[0]:
            return True
        else:
            return False
        return False


# Algorithm

# Say the area of the intersection is width * height, where width is the intersection of the rectangles projected onto the x-axis, and height is the same for the y-axis. We want both quantities to be positive.

# The width is positive when min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]), that is when the smaller of (the largest x-coordinates) is larger than the larger of (the smallest x-coordinates). The height is similar.