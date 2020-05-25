"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
            
        upcoming_search = []
        current_search = [root]

        answer_part = []
        answer = []

        while len(current_search) > 0:
            for node in current_search:
                answer_part.append(node.val)
                upcoming_search.extend(node.children)

            answer.append(answer_part)
            answer_part = []

            current_search = upcoming_search
            upcoming_search = []
        
        return answer