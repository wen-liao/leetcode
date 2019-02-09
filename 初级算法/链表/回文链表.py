# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        l1 = head
        N = 0
        while l1 != None:
            l1 = l1.next
            N += 1
        l1 = head
        for i in range(int((N+1)/2)):
            l1 = l1.next
        l2,head = head,l1
        
        #now @head is the head of the list to be reversed
        if int(N/2) > 1:
            p,q = head,head.next
            p.next,q.next,p,q = None,p,q,q.next
            while q != None:
                q.next,p,q = p,q,q.next
            l1 = p
            
        for i in range(int(N/2)):
            if not l1.val == l2.val:
                return False
            l1,l2 = l1.next,l2.next
        return True