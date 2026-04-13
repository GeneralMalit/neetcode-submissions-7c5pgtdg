# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2
        dummy = ListNode(0)
        curr = dummy
        while ptr1 and ptr2:
            tmp1, tmp2 = ptr1.next, ptr2.next
            if ptr1.val > ptr2.val:
                curr.next = ptr2
                curr = curr.next
                ptr2 = tmp2
            else:
                curr.next = ptr1
                curr = curr.next
                ptr1 = tmp1

        if ptr1:
            curr.next = ptr1
        if ptr2:
            curr.next = ptr2
        return dummy.next
            