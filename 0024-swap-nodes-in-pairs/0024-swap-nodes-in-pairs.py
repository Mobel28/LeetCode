# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while head and head.next:
            i=head
            j=head.next
            prev.next=j
            i.next=j.next
            j.next=i
            prev=i
            head=i.next
        return dummy.next