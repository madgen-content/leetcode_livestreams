# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def tree_to_list(root, mylist):
    mylist.append(root.val)

    if root.left:
        tree_to_list(root.left, mylist)
    
    if root.right:
        tree_to_list(root.right, mylist)
    return

def replace_with_sums(root, hashref):
    root.val = hashref[root.val]
    if root.left:
        replace_with_sums(root.left, hashref)
    
    if root.right:
        replace_with_sums(root.right, hashref)
    return

# this doesn't use tree principles very well
# but i'm pretty sure it's easy and fast
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        listform = []
        tree_to_list(root, listform)
        listform.sort(reverse=True)

        running_sum = listform[::]
        hash_ref = {}

        for i in range(1, len(listform)):
            running_sum[i] += running_sum[i-1]
            hash_ref[listform[i]] = running_sum[i]
        
        hash_ref[listform[0]] = listform[0]

        replace_with_sums(root, hash_ref)

        return root


# tree-based soln

def get_greatest_node(root):
    while root.right:
        root = root.right
    
    return root

def build_parent_hashmap(parent, root, hashmap):
    hashmap[root] = parent

    if root.left:
        build_parent_hashmap(root, root.left, hashmap)
    
    if root.right:
        build_parent_hashmap(root, root.right, hashmap)
    return

def is_left_child(parentmap, node):
    parent = parentmap[node]

    if parent is None:
        return None 

    return parent.left == node

def predecessor(parentmap, root):
    if root.left:
        return get_greatest_node(root.left)
    else:
        while is_left_child(parentmap, root):
            root = parentmap[root]
        return parentmap[root]

    
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        bignode = get_greatest_node(root)

        parentmap = {}
        build_parent_hashmap(None, root, parentmap)
        
        running_sum = 0

        cur = bignode
        while cur:
            cur.val += running_sum
            running_sum = cur.val
            cur = predecessor(parentmap, cur)

        return root



# java soln from YWANES
class Solution {
    public int p=0;
    public void me(TreeNode root)
    {
        p+=root.val;
        root.val=p;
    }
    public TreeNode bstToGst(TreeNode root) {  
        if ( root.left == null && root.right == null )
        {
            me(root);
            return root;        
        }
        if ( root.left != null && root.right == null )
        {
                me(root);
                bstToGst(root.left);
            return root;        
        }
        if ( root.left == null && root.right != null )
        {
                bstToGst(root.right);
                me(root);
            return root;        
        }
        bstToGst(root.right);
        me(root);
        bstToGst(root.left);
        return root;        
    }
}

# well i overdid this
class Solution:
    val = 0
    def bstToGst(self, root):
        if root.right: self.bstToGst(root.right)
        root.val = self.val = self.val + root.val
        if root.left: self.bstToGst(root.left)
        return root