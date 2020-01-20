# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_lvs(lvs: list, root: TreeNode):
    if root.left == None and root.right == None:
        lvs.append(root.val)
        return
    
    if root.left:
        build_lvs(lvs, root.left)
    
    if root.right:
        build_lvs(lvs, root.right)

    return

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return False
        
        lvs1, lvs2 = [], []

        build_lvs(lvs1, root1)
        build_lvs(lvs2, root2)

        if len(lvs1) != len(lvs2):
            return False
        
        for i in range(len(lvs1)):
            if lvs1[i] != lvs2[i]:
                return False
        return True