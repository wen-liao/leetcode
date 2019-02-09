# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None or head.next.next == None:
            return False
        p1,p2 = head.next,head.next.next
        while p1 != p2:
            if p2.next == None or p2.next.next == None:
                return False
            p1,p2 = p1.next,p2.next.next
        return True