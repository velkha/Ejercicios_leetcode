# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
                
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            current.next = ListNode(new_val)
            current = current.next
            
            # Move to the next nodes in the list
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next