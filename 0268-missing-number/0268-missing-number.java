class Solution {
    public int missingNumber(int[] nums) {
       Set<Integer> set=new HashSet<>();
       for(int n:nums){
        set.add(n);
       }
       int result=0; 
       for(int i=0;i<=nums.length;i++){
        if(!set.contains(i)){
            result=i;
        }
       }
       return result;
    }
}