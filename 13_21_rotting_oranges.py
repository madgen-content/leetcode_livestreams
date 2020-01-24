# let all start locations grow towards each other to 
# prevent going over same squares unnecessarily

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

def bfs_solve(grid, rot_starts):
    limx = len(grid[0])
    limy = len(grid)

    exploration_buffer = []
    for row, col in rot_starts:
        search_start =  explore_location(grid, limx, limy, row, col, 0)
        exploration_buffer.extend(search_start)

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
        bfs_solve(grid, rot_locations)

        # iterate array, tracking smallest number > 0
        max_gt_two = float(2)
        for r in grid:
            for v in r:
                if v == 1:
                    return -1
                if v > max_gt_two:
                    max_gt_two = v
        
        return max_gt_two - 3


# BETTER SOLN FROM LEETCODE
# better at stopping search
# does 1 level of bfs at each rotten location before moving on
def orangesRotting(self, grid: List[List[int]]) -> int:
        
        self.res = 0 
        
        rottens = []
        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    rottens.append((i,j))
        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        
        while(len(rottens)>0):
            stack = []
            len_ = len(rottens)
            for i in range(len_):
                x, y = rottens.pop()
                for dx, dy in directions:
                    row, col = x+dx, y+dy
                    if row<0 or row>=n or col<0 or col>=m or grid[row][col]!=1:
                        continue
                    grid[row][col] =2 
                    stack.append((row, col))
            if len(stack):
                self.res+=1
            rottens=stack[:]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return self.res