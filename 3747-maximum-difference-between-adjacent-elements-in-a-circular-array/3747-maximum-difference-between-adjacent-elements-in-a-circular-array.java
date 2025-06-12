class Solution {
    public int maxAdjacentDistance(int[] nums) {
       int max=0;
       for(int i=0;i<nums.length;i++){
        int nelem=(i+1)%nums.length;
        int m=Math.abs(nums[i]-nums[nelem]);
        max=Math.max(m,max);
       } 
       return max;
    }
}