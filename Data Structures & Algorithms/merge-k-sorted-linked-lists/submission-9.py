# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        dummy = ListNode()
        curr = dummy

        for idx, node in enumerate(lists):
            heapq.heappush(min_heap, (node.val, idx, node))
        
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

            curr.next = node
            curr = curr.next
        
        return dummy.next