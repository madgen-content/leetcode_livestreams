# (id, parent, rank)
class UnionFind():
    elements = None

    def __init__(self, length):
        self.elements = [[i, i, 0] for i in range(length)]
    
    def find(self, val):
        elem = self.elements[val]
        start = elem

        while elem[1] != elem[0]:
            elem = self.elements[elem[1]]
        finish = elem

        # do path compression
        start[1] = finish[0]

        return finish[0]
    
    def union(self, val1, val2):
        # path compress the vals
        v1_root_id = self.find(val1)
        v2_root_id = self.find(val2)

        # cancel if already unioned
        if v1_root_id == v2_root_id:
            return
        
        # get defining elements
        elem1 = self.elements[v1_root_id]
        elem2 = self.elements[v2_root_id]

        # determine which has higher rank
        smaller, bigger = list(sorted([elem1, elem2], key=lambda x: x[2]))

        # attach smaller to bigger
        smaller[1] = bigger[0]

        # manipulate rank as appropriate
        if smaller[2] == bigger[2]:
            bigger[2] += 1
        
        return

    # specialized for this problem
    def num_groups(self):
        gs = 0
        for elem in self.elements:
            if elem[1] == elem[0]:
                gs += 1
            
        return gs


def build_subgrid_list(grid):

    ret = []
    for row in grid:
        for letter in row:
            if letter == ' ':
                ret.extend([' ', ' ', ' ', ' '])
            elif letter == '\\':
                ret.extend([None, 'tr', 'bl', None])
            elif letter == '/':
                ret.extend(['tl', None, None, 'br'])
            
    return ret

def subgrid_look_dir(rows, cols, direction, i):
    subrows = rows * 2
    subcols = cols * 2 
    subsquares_in_row = subcols * 2
    total_elem = subrows * subcols
    
    subsquare = i % 4
    sub_rightside = (subsquare % 2) == 1
    sub_toprow = subsquare < 2 
    rowlevel_subsqare = i % subsquares_in_row
    
    ret_id = -1
    if direction == "up":
        if sub_toprow:
            ret_id = i - subsquares_in_row + 2
        else:
            ret_id = i - 2
    elif direction == "down":
        if sub_toprow:
            ret_id = i + 2
        else:
            ret_id = i + subsquares_in_row - 2
    elif direction == "left":
        if (rowlevel_subsqare == 0) or (rowlevel_subsqare == 2):
            return None
        if sub_rightside:
            ret_id = i - 1
        else:
            ret_id = i - 3
    elif direction == "right":
        if rowlevel_subsqare == (subsquares_in_row - 1) or rowlevel_subsqare == (subsquares_in_row - 3):
            return None
        if sub_rightside:
            ret_id = i + 3
        else:
            ret_id = i + 1
    

    if ret_id >= 0 and ret_id < total_elem:
        return ret_id
    
    return None 


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        subgrid_list = build_subgrid_list(grid)
        num_elems = len(subgrid_list)

        union_find = UnionFind(num_elems)

        for i in range(num_elems):
            subsquare_val = subgrid_list[i]
            if subsquare_val == ' ':
                for direction in ['up', 'down', 'left', 'right']:
                    neighbor_id = subgrid_look_dir( rows, cols, direction, i)
                    if neighbor_id is not None:
                        neighbor = subgrid_list[neighbor_id]
                        if neighbor == ' ':
                            union_find.union(i, neighbor_id)
            elif subsquare_val is not None:
                if 't' in subsquare_val:
                    neighbor_id = subgrid_look_dir( rows, cols, 'up', i)
                    if neighbor_id is not None:
                        neighbor = subgrid_list[neighbor_id]
                        if neighbor is not None and (neighbor == ' ' or ('b' in neighbor)):
                            union_find.union(i, neighbor_id)
                elif 'b' in subsquare_val:
                    neighbor_id = subgrid_look_dir( rows, cols, 'down', i)
                    if neighbor_id is not None:
                        neighbor = subgrid_list[neighbor_id]
                        if neighbor is not None and (neighbor == ' ' or ('t' in neighbor)):
                            union_find.union(i, neighbor_id)
                
                if 'l' in subsquare_val:
                    neighbor_id = subgrid_look_dir( rows, cols, 'left', i)
                    if neighbor_id is not None:
                        neighbor = subgrid_list[neighbor_id]
                        if neighbor is not None and (neighbor == ' ' or ('r' in neighbor)):
                            union_find.union(i, neighbor_id)
                elif 'r' in subsquare_val:
                    neighbor_id = subgrid_look_dir( rows, cols, 'right', i)
                    if neighbor_id is not None:
                        neighbor = subgrid_list[neighbor_id]
                        if neighbor is not None and (neighbor == ' ' or ('l' in neighbor)):
                            union_find.union(i, neighbor_id)
            else:
                if (i % 4) == 1 or (i % 4) == 2:
                    for direction in ['up', 'left']:
                        neighbor_id = subgrid_look_dir( rows, cols, direction, i)
                        if neighbor_id is not None:
                            neighbor = subgrid_list[neighbor_id]
                            if neighbor is not None:
                                union_find.union(i, neighbor_id)
                else:
                    for direction in ['up', 'right']:
                        neighbor_id = subgrid_look_dir( rows, cols, direction, i)
                        if neighbor_id is not None:
                            neighbor = subgrid_list[neighbor_id]
                            if neighbor is not None:
                                union_find.union(i, neighbor_id)


        
        return union_find.num_groups()