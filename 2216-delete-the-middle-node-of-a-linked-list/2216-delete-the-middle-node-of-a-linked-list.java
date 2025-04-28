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
    public ListNode deleteMiddle(ListNode head) {
        if(head==null||head.next==null)return null;
        ListNode prev=null;
        ListNode strt=head;
        ListNode end=head;
        while(end!=null && end.next!=null){
            prev=strt;
            strt=strt.next;
            end=end.next.next;
        }
       prev.next=strt.next;
       return head;
    }
}