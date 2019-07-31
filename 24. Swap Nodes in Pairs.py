# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        pre_first = ListNode(0)
        pre_first.next  = head
        pre_head        = pre_first
        first           = None
        second          = None
        pos_second      = None
        current         = head
        while current is not None:
            if i % 2 == 0:
                first   = current
                current = current.next
            else:
                second          = current
                current         = current.next
                pos_second      = second.next 
                pre_first.next  = second
                second.next     = first
                first.next      = pos_second
                pre_first       = first
            i = i + 1
        return pre_head.next














