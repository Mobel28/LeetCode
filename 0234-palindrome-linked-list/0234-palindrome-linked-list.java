/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode strt=head ,end=head;
        while(end!=null && end.next !=null){
            strt=strt.next;
            end=end.next.next;
        }
        ListNode prev=null , curr=strt;
        while(curr!=null){
            ListNode temp=curr.next;
            curr.next=prev;
            prev=curr;
            curr=temp;
        }
        ListNode i=head,j=prev;
        while(j!=null){
            if(i.val!=j.val){
                return false;
            }
            i=i.next;
            j=j.next;
        }
        return true;
    }
}