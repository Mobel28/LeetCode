# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1=""
        while l1:
            r1+=str(l1.val)
            l1=l1.next
        r2=""
        while l2:
            r2+=str(l2.val)
            l2=l2.next
        r1=r1[::-1]
        r2=r2[::-1]
        res=str(int(r1)+int(r2))
        res=res[::-1]
        flist=ListNode(0)
        curr=flist
        for i in res:
            c=ListNode(int(i))
            curr.next=c
            curr=curr.next
        return flist.next