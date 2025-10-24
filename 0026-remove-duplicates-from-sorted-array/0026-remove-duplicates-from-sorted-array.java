class Solution {
    public int removeDuplicates(int[] nums) {
        int count=0;
      for(int i=0;i<nums.length;i++){
        if(nums[i]==nums[count]){
            continue;
        }
        else{
            count++;
            nums[count]=nums[i];
        }
      }
      return count+1;  
    }
}