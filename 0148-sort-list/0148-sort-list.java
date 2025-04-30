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
    public ListNode sortList(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode mid=mid(head);
        ListNode left=sortList(head);
        ListNode right=sortList(mid);
        return merge(left,right);
    }
    private ListNode mid(ListNode head){
        ListNode i=head ,j=head ,prev=null;
        while(j!=null &&j.next!=null){
            prev=i;
            i=i.next;
            j=j.next.next;
        }
        if(prev!=null)prev.next=null;
        return i;
    }
    private ListNode merge(ListNode l1,ListNode l2){
        ListNode dummy=new ListNode(0);
        ListNode t=dummy;
        while(l1!=null && l2!=null){
            if(l1.val<l2.val){
                t.next=l1;
                l1=l1.next;
            }
            else{
                t.next=l2;
                l2=l2.next;
            }
            t=t.next;
        }
        t.next=(l1!=null)?l1:l2;
        return dummy.next;
    }

}