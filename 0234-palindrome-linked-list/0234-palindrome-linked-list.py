# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sta=[]
        curr=head
        while curr:
            sta.append(curr.val)
            curr=curr.next
        curr=head
        while curr:
            if sta.pop()!=curr.val:
                return False
            curr=curr.next
        return True