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
    public int getDecimalValue(ListNode head) {
        StringBuilder res=new StringBuilder();
        while(head!=null){
            res.append(head.val);
            head=head.next;
        }
        int r=0;
        for(char c:res.toString().toCharArray()){
            r=r*2+(c-'0');
        }
        return r;
    }
}