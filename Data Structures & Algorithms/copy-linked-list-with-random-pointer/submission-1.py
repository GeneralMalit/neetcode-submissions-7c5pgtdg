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
            temp = curr.next
            copy = Node(curr.val)
            copy.next = temp
            curr.next = copy
            curr = temp

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        dummy = Node(0)
        nl = dummy
        while curr:
            temp = curr.next
            orig = temp.next
            curr.next = orig
            curr = orig
            nl.next = temp
            nl = temp
        

        return dummy.next