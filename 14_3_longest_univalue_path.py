# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    

def base_explore(root, candidates):
    if root.left:
        explore(root, root.left, 0, 0, candidates)
    if root.right: 
        explore(root, root.right, 0, 0, candidates)
    return

def explore(parent, root: TreeNode, cur_depth: int, cur_maxlen: int, candidates: list):
    if root.val == parent.val:
        next_depth = cur_depth + 1
    else:
        next_depth = 0
    
    cur_maxlen = max(next_depth, cur_maxlen)

    if root.left:
        explore(root, root.left, next_depth, cur_maxlen, candidates)
    
    if root.right: 
        explore(root, root.right, next_depth, cur_maxlen, candidates)
    
    if root.left == None and root.right == None:
        candidates.append(cur_maxlen)

    return

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root.left == None and root.right == None:
            return 0
        
        candidates = []
        base_explore(root, candidates)

        return max(candidates)