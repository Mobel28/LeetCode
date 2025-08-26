# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length=1
        temp=head
        while temp.next:
            length+=1
            temp=temp.next
        temp.next=head
        k=k%length
        if k==0:
            temp.next=None
            return head
        taillength=length-k
        newtail=head
        for _ in range(taillength-1):
            newtail=newtail.next
        newhead=newtail.next
        newtail.next=None
        return newhead