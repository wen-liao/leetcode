# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p,q = head, head.next
        p.next,q.next,p,q = None,p,q,q.next
        while q != None:
            q.next,p,q = p,q,q.next
        head = p
        return head