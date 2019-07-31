# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return l1 or l2
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        current = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                current = l1
                l1=l1.next
            else:
                current.next = l2
                current = l2
                l2=l2.next
        if l1 is not None:
            current.next = l1
        if l2 is not None:
            current.next = l2
        return head







