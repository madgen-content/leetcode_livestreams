# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# weird degenerate situation when hitting node with val zero
# must move forward at least one more
# this is fine though, because guarantee that 
# zero is not at the intersection
def fix_list(p):
    while p != None:
        if p.val <= 0:
            p.val = p.val * -1
            p = p.next
        else:
            return
    return

def fix_both(a, b):
    fix_list(a)
    fix_list(b)
    return

# It's faster to listify than to tuplify for marking nodes as explored!
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
            
        p1 = headA
        p2 = headB

        if p1 == p2:
            return p1

        while True:
            if p1 != None:
                if p1.val < 0:
                    fix_both(headA, headB)
                    return p1
                else:
                    p1.val = p1.val * -1
                    p1 = p1.next
            
            if p2 != None:
                if p2.val < 0:
                    fix_both(headA, headB)
                    return p2
                else:
                    p2.val = p2.val * -1
                    p2 = p2.next
            
            if p1 == None and p2 == None:
                fix_both(headA, headB)
                return None


# alternative clever soln
# use symmetry, run through both with both pointers
# if intersects, guaranteed to catch up with each other
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        if headA is headB:
            return headA
        
        runnerA = headA
        runnerB = headB
        
        # This condition will eaither break when:
        #   1) Found an intersection
        #   2) On 2nd pass through both runners are exhausted and
        #       are now `None`
        while runnerA is not runnerB:
            if runnerA:
                runnerA = runnerA.next
            else:
                # Restart runner on head of other list.
                runnerA = headB
                
            if runnerB:
                runnerB = runnerB.next
            else:
                # Once both runners have been reassigned they are
                # exactly the same distance from their tail nodes.
                runnerB = headA
        return runnerA