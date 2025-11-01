# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        rem=set(nums)
        dummy.next=head
        prev,curr=dummy,head
        while curr:
            if curr.val in rem:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return dummy.next
