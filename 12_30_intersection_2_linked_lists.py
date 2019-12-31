# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def fix_list(p):
    while p != None:
        if isinstance(p.val, list):
            p.val = p.val[0]
        p = p.next
    return

def fix_both(a, b):
    fix_list(a)
    fix_list(b)
    return

# It's faster to listify than to tuplify for marking nodes as explored!
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        p1 = headA
        p2 = headB

        if p1 == p2:
            return p1

        while True:
            if p1 != None:
                if isinstance(p1.val, list):
                    fix_both(headA, headB)
                    return p1
                else:
                    p1.val = [p1.val,]
                    p1 = p1.next
            
            if p2 != None:
                if isinstance(p2.val, list):
                    fix_both(headA, headB)
                    return p2
                else:
                    p2.val = [p2.val,]
                    p2 = p2.next
            
            if p1 == None and p2 == None:
                fix_both(headA, headB)
                return None

            
            


