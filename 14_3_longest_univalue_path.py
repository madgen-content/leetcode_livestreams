# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    

def explore(root: TreeNode, matchval: int, pathsize: list, candidates: list):
    if root.val == matchval:
        pathsize[0] += 1
        if root.left:
            explore(root.left, matchval, pathsize, candidates)
    
        if root.right: 
            explore(root.right, matchval, pathsize, candidates)
    else:
        newpathsize = [0]
        if root.left:
            explore(root.left, root.val, newpathsize, candidates)
    
        if root.right:
            explore(root.right, root.val, newpathsize, candidates)
        
        candidates.append(newpathsize[0])
    
    return

def printtree(root):
    print(root.val)

    if root.left:
        print("L")
        printtree(root.left)
    else:
        print('ldone')

    if root.right:
        print("R")
        printtree(root.right)
    else:
        print('rdone')
    return

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root == None or (root.left == None and root.right == None):
            return 0
        
        printtree(root)
        
        candidates = []
        explore(root, -1, [-1], candidates)

        return max(candidates)