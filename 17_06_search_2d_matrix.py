def can_contain_target(mat, target, tl_coord, br_coord):
    i,j = tl_coord
    m,n = br_coord
    
    lb = mat[i][j]
    ub = mat[m][n]

    if target >= lb and target <= ub:
        return True
    else:
        return False
    return

def valid_corners(mat, corners):
    tl, br = corners
    i,j = tl
    m,n = br

    maxrow = len(mat)
    maxcol = len(mat[0])

    if i < maxrow and m < maxrow and j < maxcol and n < maxcol:
        if m >= i and n >=j:
            return True
        else:
            return False
    else:
        return False
    return

def get_submatrix_coords(mat, tl_coord, br_coord, center_coord):
    
    i,j = tl_coord
    m,n = br_coord
    r,s = center_coord

    I = ((i,j),(r,s))
    II = ((i,s+1), (r,n))
    III = ((r+1,j), (m, s))
    IV = ((r+1, s+1), (m,n))
    submatrix_corners = [I, II, III, IV]

    submatrix_corners = [corners for corners in submatrix_corners if valid_corners(mat, corners)]
    return submatrix_corners

# coords are (row, col) tuples
def rec_mat_search(mat, target, tl_coord, br_coord):
    i, j = tl_coord
    m, n = br_coord

    if i == m and j == n:
        return mat[i][j] == target

    mid_row = (i + m) // 2
    mid_col = (j + n) // 2
    mid_coord = (mid_row, mid_col)

    if mat[mid_row][mid_col] == target:
        return True
    else:
        submatrices = get_submatrix_coords(mat, tl_coord, br_coord, mid_coord)
        for corners in submatrices:
            if can_contain_target(mat, target, corners[0], corners[1]):
                result = rec_mat_search(mat, target, corners[0], corners[1])
                if result == True:
                    return True
    return False

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        return rec_mat_search(matrix, target, (0,0), (len(matrix)-1, len(matrix[0])-1) )

# ==========================================
# ywanes's JAVA soln, MUCH BETTER. much simpler
# I didn't think about the other corners enough

class Solution { public boolean searchMatrix(int[][] matrix, int target) { 
    int x=matrix.length-1;
    int y=0;
    while(true) { if ( x < 0 || y >= matrix[0].length ) return false;
    if ( matrix[x][y] == target ) return true;
    if ( matrix[x][y] < target ) y++;
    else x--;
    } } 
}