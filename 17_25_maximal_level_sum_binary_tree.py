# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs_sumlist(rowsums, depth, node):
    if depth > len(rowsums):
        rowsums.append(0)

    rowsums[depth-1] += node.val

    if node.left is not None:
        dfs_sumlist(rowsums, depth + 1, node.left)
    
    if node.right is not None:
        dfs_sumlist(rowsums, depth + 1, node.right)

    return

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root == None: return 0
        if root.left == None and root.right == None: return 1

        rowsums = []
        dfs_sumlist(rowsums, 1, root)

        return rowsums.index(max(rowsums)) + 1

# discussion board answer
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levels, l, q = [], 1, [root]
        while q:
            levels.append([sum(node.val for node in q), l])
            l += 1
            q = [child for node in q for child in (node.left, node.right) if child]
        return sorted(levels, key = lambda x: (x[0], -x[1]))[-1][1]