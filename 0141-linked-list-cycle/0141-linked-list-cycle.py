# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i=head
        j=head
        while i and i.next:
            i=i.next.next
            j=j.next
            if i==j:
                return True
        return False