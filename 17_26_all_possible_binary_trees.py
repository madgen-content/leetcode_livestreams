# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def deep_tree_copy(root):
    new_root = TreeNode()

    if root.left is not None:
        new_root.left = deep_tree_copy(root.left)
    
    if root.right is not None:
        new_root.right = deep_tree_copy(root.right)

    return new_root

def tree_to_bools(root, buf):

    if root.left is None:
        buf.append(False)
    else:
        buf.append(True)
        tree_to_bools(root.left, buf)
    
    if root.right is None:
        buf.append(False)
    else:
        buf.append(True)
        tree_to_bools(root.right, buf)
    
    return tuple(buf)


def recursive_build_trees(answer, N, cur_count, root, current_node):
    if current_node.left is None and current_node.right is None:
        current_node.left = TreeNode()
        current_node.right = TreeNode()
        treecopy = deep_tree_copy(root)
        current_node.left = None
        current_node.right = None

        new_count = cur_count+2

        if new_count == N:
            tree_id = tree_to_bools(treecopy, [True])
            answer[tree_id] = treecopy
            return
        else:
            recursive_build_trees(answer, N, new_count, treecopy, treecopy)            

    else:
        recursive_build_trees(answer, N, cur_count, root, current_node.left) 
        recursive_build_trees(answer, N, cur_count, root, current_node.right) 
    return

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:

        answer = {}
        count = 1
        root = TreeNode()

        recursive_build_trees(answer, N, count, root, root)
        return answer.values()