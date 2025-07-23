class Solution {
    public int findDuplicate(int[] nums) {
        HashSet<Integer> pnum=new HashSet<>();
        int res=-1;
        for(int i=0;i<nums.length;i++){
            if(pnum.contains(nums[i])){
                res=nums[i];
            }
            else{
                pnum.add(nums[i]);
            }
        }
        return res;
    }
}