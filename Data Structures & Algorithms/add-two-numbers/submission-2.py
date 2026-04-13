# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while carry or l1 or l2:
            l1_v = l1.val if l1 else 0
            l2_v = l2.val if l2 else 0
            
            total = l1_v + l2_v + carry

            carry = total // 10 
            new = ListNode(total % 10)
            curr.next = new
            curr = curr.next

            if l1: 
                l1 = l1.next
            
            if l2:
                l2 = l2.next

        return dummy.next
            
