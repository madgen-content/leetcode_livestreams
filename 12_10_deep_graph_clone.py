# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

# IDEA NOTES:
    # 1. mutate graph during exploration; mark explored
    # 2. Use DFS
    # 3. be sure to immediately add parent to list of neighbors
    # 4. nodes given to us are 'external' 
    # 5. structure we're creating is 'internal'

def build_recursive(external_node):
    # tie the not in the case of a loop
    if isinstance(external_node.val, Node):
        return external_node.val

    # create new part of our new structure
    internal_node = Node(external_node.val, [])

    # jank way of marking external object as explored
    # also allows us to tie the knot without a linear search
    external_node.val = internal_node
    
    for external_child in external_node.neighbors:
        internal_node.neighbors.append(build_recursive(external_child))
    
    return internal_node

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return build_recursive(node)