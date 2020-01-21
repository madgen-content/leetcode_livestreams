
def explore_location(grid, limx, limy, row, col, rot_time):
    val = grid[row][col]
    rot_signal = rot_time + 3

    if val == 0 or (val == 2 and rot_signal > 3):
        return []

    extends = []
    if val > rot_signal or val == 1 or val == 2:
        grid[row][col] = rot_signal
        if row - 1 >= 0:
            extends.append((row - 1, col, rot_time + 1))
        if col - 1 >= 0:
            extends.append((row, col - 1, rot_time + 1))
        if row + 1 < limy:
            extends.append((row + 1, col, rot_time + 1))
        if col + 1 < limx:
            extends.append((row, col + 1, rot_time + 1))

    return extends

def bfs_location(grid, row, col):
    limx = len(grid[0])
    limy = len(grid)

    exploration_buffer = explore_location(grid, limx, limy, row, col, 0)

    while len(exploration_buffer) > 0:
        row, col, rot_time = exploration_buffer[0]
        new_explorations = explore_location(grid, limx, limy, row, col, rot_time)
        exploration_buffer.extend(new_explorations)
        del exploration_buffer[0]
    return

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # get all initial rot locations, count fresh
        rot_locations = []
        fresh_count = 0

        for i in range(len(grid)):
            r = grid[i]
            for j in range(len(r)):
                v = r[j]
                if v == 2:
                    rot_locations.append((i,j))
                if v == 1:
                    fresh_count += 1

        # short circuit for missing rots and missing fresh
        if fresh_count == 0:
            return 0

        if len(rot_locations) == 0:
            return -1
        
        # explore rots
        for r, c in rot_locations:
            bfs_location(grid, r, c)

        # iterate array, tracking smallest number > 0
        max_gt_two = float(2)
        for r in grid:
            for v in r:
                if v == 1:
                    return -1
                if v > max_gt_two:
                    max_gt_two = v
        
        return max_gt_two - 3