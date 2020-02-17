# Definition for singly-linked list.
class ListNode:
    self.val = None
    self.next  = None

    def __init__(self, x):
        self.val = x
        self.next = None

def get_tail_and_len(head):
    length = 0
    while head.next != None:
        head = head.next
        length +=1

    return head, length

def cycle_to_front(cur_head: ListNode, cycle_node: ListNode, cycle_prev: ListNode):

    cycle_prev.next = cycle_node.next
    cycle_node.next = cur_head
    return cycle_node

def cycle_to_back(cur_tail: ListNode, cycle_node: ListNode, cycle_prev: ListNode):
    
    cycle_prev.next = cycle_node.next
    cur_tail.next = cycle_node
    cycle_node.next = None
    return cycle_node

def partition_list(head, x):
    cur_head = head
    cur_tail, length = get_tail_and_len(head)

    itrs = 0
    tail_cycles = 0
    prev = None
    upcoming = head
    while upcoming != None and length - tail_cycles > itrs:
        itrs += 1
        cur = upcoming
        upcoming = upcoming.next

        if cur.val < x and cur != cur_head:
            cur_head = cycle_to_front(cur_head, cur, prev)
            continue
        
        if cur.val > x and cur != cur_tail:
            cur_tail = cycle_to_back(cur_tail, cur, prev)
            tail_cycles += 1
            continue

        prev = cur

    return cur_head

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        return partition_list(head, x)

# Abandon ship - do sensible soln
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None or head.next == None:
            return head

        lower = []
        upper = []

        while head != None:
            if head.val < x:
                lower.append(head)
            else:
                upper.append(head)
            head = head.next
        
        lower.extend(upper)

        for i in range(len(lower)-1):
            node = lower[i]
            nxt = lower[i+1]

            node.next = nxt
        
        lower[-1].next = None

        return lower[0]