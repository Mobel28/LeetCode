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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) {
            return head;
        }
        int l=1;
        ListNode tail=head;
        while(tail.next!=null){
            l++;
            tail=tail.next;
        }
        k=k%l;
        if(k==0){
            return head;
        }
        ListNode newt=head;
        for(int i=0;i<l-k-1;i++){
            newt=newt.next;
        }
        ListNode newh=newt.next;
        newt.next=null;
        tail.next=head;
        return newh;
    }

}