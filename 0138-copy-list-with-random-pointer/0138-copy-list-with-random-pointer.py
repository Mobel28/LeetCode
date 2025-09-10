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
        if not head:
            return None
        curr=head
        while curr:
            node=Node(curr.val,curr.next,curr.random)
            curr.next=node
            curr=node.next
        curr=head
        while curr:
            if curr.random:
                curr.next.random=curr.random.next
            curr=curr.next.next
        curr=head
        copy=head.next
        while curr:
            c=curr.next
            curr.next=c.next
            if c.next:
                c.next=c.next.next
            curr=curr.next
        return copy
    
    
    