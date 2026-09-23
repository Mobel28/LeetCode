class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
       ArrayList <List<Integer>> res=new ArrayList<>();
       Arrays.sort(nums);
       for (int i=0;i<nums.length;i++){
        if (i>0 && nums[i-1]==nums[i]){
            continue;
        }
        int left=i+1;
        int right=nums.length-1;
        while (left<right){
            int total=nums[left]+nums[right]+nums[i];
            if (total==0){
                res.add(Arrays.asList(nums[i],nums[left],nums[right]));
            
                while (left<right && nums[left]==nums[left+1]){
                    left+=1;
                }
                while (left<right && nums[right]==nums[right-1]){
                    right-=1;
                }
                left+=1;
                right-=1;
            }
            else if (total<0){
                left++;
            }
            else{
                right--;
            }
        }
       } 
       return res ;
    }
}