# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        dummy=res
        c=0
        while l1 or l2 or c!=0:
            s=c
            if l1:
                s+=l1.val
                l1=l1.next
            if l2:
                s+=l2.val
                l2=l2.next
            dummy.next=ListNode(s%10)
            c=s//10
            dummy=dummy.next
        return res.next
