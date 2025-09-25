# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer=[]
        temp=head
        while temp:
            mov = temp.next
            while mov and mov.val <= temp.val:
                mov = mov.next
            if mov:
                answer.append(mov.val)
            else:
                answer.append(0)
            temp = temp.next 
        return answer