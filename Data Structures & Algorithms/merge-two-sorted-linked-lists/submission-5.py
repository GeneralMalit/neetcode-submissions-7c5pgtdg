# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        dummy = ListNode(0, 0)
        curr = dummy
        while list1 and list2:
            tmp1, tmp2 = list1.next, list2.next
            if list1.val > list2.val:
                curr.next = list2
                curr = curr.next
                list2 = tmp2
            else:
                curr.next = list1
                curr = curr.next
                list1 = tmp1
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next
