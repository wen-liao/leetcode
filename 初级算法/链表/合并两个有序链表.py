class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            ret,l1 = l1,l1.next
        else:
            ret,l2 = l2,l2.next
        ret.next = self.mergeTwoLists(l1,l2)
        return ret