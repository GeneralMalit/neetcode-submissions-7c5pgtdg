# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        
        while l1 or l2:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            total = carry + l1v + l2v

            num = total % 10
            carry = total // 10

            curr.next = ListNode(num)

            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next