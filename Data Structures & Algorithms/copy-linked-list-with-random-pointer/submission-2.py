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
            temp = curr.next
            curr.next = copy
            copy.next = temp
            curr = temp
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        dummy = Node(0)
        l2 = dummy
        curr = head
        while curr:
            copy = curr.next
            orig = copy.next
            l2.next = copy
            curr.next = orig
            l2, curr = copy, orig
        return dummy.next


    
