def get_neighbors(board, i, j):
    lb = 0
    rb = len(board[0]) - 1
    tb = 0
    bb = len(board) - 1

    all_neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    good_neighbors = [x for x in all_neighbors if x[0] >= tb and x[0]<=bb and x[1] >= lb and x[1] <= rb]
    return good_neighbors

def dfs_letter(board, i, j):
    letter = board[i][j]

    if letter == "O":
        board[i][j] = "Z"
        neighbors = get_neighbors(board, i, j)
        for neighbor in neighbors:
            dfs_letter(board, neighbor[0], neighbor[1])
    
    return

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) <= 1 or len(board[0]) <=1:
            return
        
        bottom = len(board)-1
        right = len(board[0])-1

        for j in range(len(board[0])):
            dfs_letter(board, 0, j)
            dfs_letter(board, bottom, j)
        
        for i in range(len(board)):
            dfs_letter(board, i, 0)
            dfs_letter(board, i, right)

        for i in range(len(board)):
            for j in range(len(board[0])):
                letter = board[i][j]
                if letter == "O":
                    board[i][j] = "X"
                elif letter == "Z":
                    board[i][j] = "O"

        return
        