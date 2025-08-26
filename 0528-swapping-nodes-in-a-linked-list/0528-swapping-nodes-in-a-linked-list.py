# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=head
        length=1
        while dummy.next:
            dummy=dummy.next
            length+=1
        ltemp=head
        for _ in range(length-k):
            ltemp=ltemp.next
        ftemp=head
        for _ in range(k-1):
            ftemp=ftemp.next
        ftemp.val,ltemp.val=ltemp.val,ftemp.val
        return head
        