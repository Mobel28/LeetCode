class Solution {
    public boolean check(int[] nums) {
        int count=0;
        for (int i=1;i<nums.length;i++){
            if (nums[i]<nums[i-1]){
                count+=1;
            }
        }
        if (nums[0]<nums[nums.length-1]){
            count+=1;
        }
        return count<=1;
    }
}