"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        dummy = Node(0)
        copy_list = dummy
        while curr:
            copy = curr.next
            orig_next = copy.next

            copy_list.next = copy
            copy_list = copy

            curr.next = orig_next
            curr = orig_next
        return dummy.next






        return dummy.next