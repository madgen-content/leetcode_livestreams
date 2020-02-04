# my broken soln. sad day. solved wrong prollem
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

# from zombiekillerwhale!
class Solution(object):
           
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def visit_nodes(node):
            if not node:
                return
            longest_path_at_current = calc_longest_straight_univalue_path(node.left, node.val) \
                                    + calc_longest_straight_univalue_path(node.right, node.val)
            left_max = visit_nodes(node.left)
            right_max = visit_nodes(node.right)
            return max(longest_path_at_current, left_max, right_max)
       
        def calc_longest_straight_univalue_path(node, target):
            if not node or node.val != target:
                return 0
            return max(calc_longest_straight_univalue_path(node.left, node.val),
                       calc_longest_straight_univalue_path(node.right, node.val)) + 1
       
        return visit_nodes(root) if root else 0

# soln from discussion, nice.
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        longest = [0]
        def traverse(node):
            if not node:
                return 0
            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            longest[0] = max(longest[0], left + right)
            return max(left, right)
        traverse(root)
        return longest[0]