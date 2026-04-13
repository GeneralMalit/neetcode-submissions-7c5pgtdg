# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        dummy = ListNode(0)
        tail = dummy

        for i, l in enumerate(lists):
            heapq.heappush(min_heap, (l.val, i, l))

        while min_heap:
            val, i, l = heapq.heappop(min_heap)

            tail.next = l
            tail = tail.next

            if l.next:
                heapq.heappush(min_heap, (l.next.val, i, l.next))
        return dummy.next