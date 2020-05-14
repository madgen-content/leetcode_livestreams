# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        answer = []
        upcoming = []
        cur = [root]
        lr = True

        while len(cur) > 0:
            partial_ans = []

            while len(cur) > 0:
                node = cur.pop()
                partial_ans.append(node.val)
                kids = {True: node.left, False: node.right}

                if kids[lr] is not None:
                    upcoming.append(kids[lr])
                
                if kids[not lr] is not None:
                    upcoming.append(kids[not lr])
            answer.append(partial_ans)

            lr = not lr
            cur = upcoming
            upcoming = []

        return answer