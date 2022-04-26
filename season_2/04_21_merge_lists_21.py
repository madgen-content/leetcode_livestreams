# Definition for singly-linked list.
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2

        if list1.val < list2.val:
            cur = list1
            list1 = list1.next
        else:
            cur = list2
            list2 = list2.next
        
        root = cur
        while list1 or list2:

            if list2 is None:
                cur.next = list1
                break
            
            if list1 is None:
                cur.next = list2
                break

            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next

        return root