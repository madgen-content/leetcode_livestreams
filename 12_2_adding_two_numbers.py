# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# GOOD SOLN
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        node = ListNode( (l1.val + l2.val) % 10)
        head = node
        carry = (l1.val + l2.val) // 10
        if l1.next == None and l2.next == None:
            if carry > 0:
                node.next = ListNode(carry)
            return head
        l1 = l1.next
        l2 = l2.next
            
        while True:
            if l1 == None:
                v1 = 0
            else:
                v1 = l1.val
                l1 = l1.next
            
            if l2 == None:
                v2 = 0
            else:
                v2 = l2.val
                l2 = l2.next
            
            val = v1 + v2 + carry
            node.next = ListNode( val %10)
            carry = val // 10
            
            node = node.next
                
            if l1 == None and l2 == None:
                if carry > 0:
                    node.next = ListNode(carry)
                break
        return head

# BAD SOLN
def listnode_to_int(ln):
    builder = []
    while True:
        builder.append(str(ln.val))
        if ln.next == None:
            break
        ln = ln.next
    ret = int(''.join(reversed(builder)))
    return ret

def int_to_listnode(num, ):
    int_arr = list(reversed([ListNode(int(x)) for x in str(num)]))
    for i in range(len(int_arr) - 1):
        int_arr[i].next = int_arr[i+1]
    return int_arr[0]

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = listnode_to_int(l1)
        n2 = listnode_to_int(l2)
        del l1
        del l2
        result = n1 + n2
        ret = int_to_listnode(result)
        return ret