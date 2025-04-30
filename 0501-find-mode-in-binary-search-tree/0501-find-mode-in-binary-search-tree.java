/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    Integer currval=null;
    int ccount=0;
    int mcount=0;
    List<Integer> mode=new ArrayList<>();
    public int[] findMode(TreeNode root) {
        inorder(root);
        int []res=new int[mode.size()];
        for(int i=0;i<mode.size();i++){
            res[i]=mode.get(i);
        }
        return res;
    }
    public void inorder(TreeNode node){
        if(node==null)return;
        inorder(node.left);
        handleval(node.val);
        inorder(node.right);
    }
    public void handleval(int val){
        if(currval == null || val != currval){
            currval=val;
            ccount=1;
        }
        else{
            ccount++;
        }
        if(ccount>mcount){
            mcount=ccount;
            mode.clear();
            mode.add(currval);
        }
        else if(ccount==mcount){
            mode.add(currval);
        }
    }
}