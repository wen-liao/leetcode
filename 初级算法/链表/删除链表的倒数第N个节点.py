# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 1:
            p = head
            if p.next == None:
                return None
            else:
                while p.next.next != None:
                    p = p.next
                q = p.next
                p.next = None
                del(q)
                return head
        p,q = head,head
        for i in range(n):
            q = q.next
        while q != None:
            q = q.next
            p = p.next
        p.val = p.next.val
        q = p.next
        p.next = q.next
        del(q)
        return head