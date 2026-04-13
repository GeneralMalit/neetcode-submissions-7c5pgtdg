# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = None
        prev = None
        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp

        ptr1, ptr2 = head, prev
        while ptr2:
            tmp1, tmp2 = ptr1.next, ptr2.next
            ptr1.next = ptr2
            ptr2.next = tmp1
            ptr1, ptr2 = tmp1, tmp2
