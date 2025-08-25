# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        r=""
        curr=head
        while curr:
            r+=str(curr.val)
            curr=curr.next
        res = 0
        n = len(r)
        for i in range(n):
            res += int(r[i]) * (2 ** (n - i - 1)) 
        return res