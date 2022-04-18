# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pred(self,node):
        if node.left is not None:
            node = node.left
            while node.right is not None:
                node = node.right
            return node
        else:
            while node.parent is not None:
                if self.is_rchild(node):
                    return node.parent
                else:
                    node = node.parent
        return None

    def succ(self, node):
        if node.right is not None:
            node = node.right
            while node.left is not None:
                node = node.left
            return node
        else:
            while node.parent is not None:
                if self.is_lchild(node):
                    return node.parent
                else:
                    node = node.parent

        return None
    
    def is_lchild(self, node):
        if node.parent.left is node:
            return True
        else: 
            return False

    def is_rchild(self, node):
        return not self.is_lchild(node)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        root.parent = None
        buf = [root]
        i = 0
        mindiff = float('inf')
        while i < len(buf):
            r = buf[i]
            if r.right is not None:
                buf.append(r.right)
                r.right.parent = r
            if r.left is not None:
                buf.append(r.left)
                r.left.parent = r
            
            pred = self.pred(r)
            succ = self.succ(r)
            if pred is not None:
                mindiff = min(mindiff, abs(r.val - pred.val))
            if succ is not None:
                mindiff = min(mindiff, abs(r.val - succ.val))
            i+=1
        return mindiff
    # ---------------------------------------------------
    # add optimization to not redo leaves - takes perf from 5% to 60%
    # best soln is actually just putting everything in a list and diffing neighbors
    # ---------------------------------------------------
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        root.parent = None
        buf = [root]
        i = 0
        mindiff = float('inf')
        while i < len(buf):
            r = buf[i]
            i+=1
            if r.right is None and r.left is None:
                continue

            if r.right is not None:
                buf.append(r.right)
                r.right.parent = r
            if r.left is not None:
                buf.append(r.left)
                r.left.parent = r
            
            pred = self.pred(r)
            succ = self.succ(r)
            if pred is not None:
                mindiff = min(mindiff, abs(r.val - pred.val))
            if succ is not None:
                mindiff = min(mindiff, abs(r.val - succ.val))
        return mindiff