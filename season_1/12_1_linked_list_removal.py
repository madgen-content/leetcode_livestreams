class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        leader = head
        follower = head
        follower_prev = None
        leader_location = 1
        while leader.next != None:
            if leader_location >= n:
                follower_prev = follower
                follower = follower.next
            
            leader = leader.next
            leader_location +=1

        if follower == head:
            return head.next
        else:
            follower_prev.next = follower.next
            return head

        return