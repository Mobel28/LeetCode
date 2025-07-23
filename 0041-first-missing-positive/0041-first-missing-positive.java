class Solution {
    public int firstMissingPositive(int[] nums) {
       Arrays.sort(nums);
       int s=1;
       for(int n:nums){
        if(n==s){
            s++;
        }
       }
       return s;
    }
}