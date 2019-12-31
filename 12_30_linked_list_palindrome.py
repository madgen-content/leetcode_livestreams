# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from math import ceil

def findlen(p):
    len = 0
    while p != None:
        len += 1
        p = p.next
    return len

# rather than explicitly build two separate lists of the same length to compare, be better about handling the middle
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        
        listlen = findlen(head)
        
        odd_length = listlen % 2 == 1
        mid = int(ceil(listlen/2))
        chop = listlen // 2

        prev = None
        p = head
        for i in range(listlen):
            if odd_length and i == chop:
                p = p.next
                continue
            elif i < mid:
                prev = p
                p = p.next
                continue
            else:
                temp = p.next
                if i == mid:
                    prev.next = None
                    p.next = None
                else:
                    p.next = prev
                prev = p
                p = temp
        
        headA = head
        headB = prev

        # guaranteed to have 2 equal length lists

        while headA != None:
            if headA.val != headB.val:
                return False
            headA = headA.next
            headB = headB.next

        return True

# this solution is similar but much smoother
# the tuple unpacking makes me wanna die though
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head and head.next:
            # get middle of list
            mid = fast = head
            while fast and fast.next:
                mid, fast = mid.next, fast.next.next
            
            # reverse second half
            rev, n2, mid.next = mid, mid.next, None
            while n2:
                tmp, n2.next = n2.next, rev
                rev, n2 = n2, tmp
            
            # pair-wise comparison
            while head and rev:
                if head.val != rev.val:
                    return False
                head, rev = head.next, rev.next
                
        return True
