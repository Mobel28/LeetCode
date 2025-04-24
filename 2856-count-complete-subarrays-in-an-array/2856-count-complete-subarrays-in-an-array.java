class Solution {
    public int countCompleteSubarrays(int[] nums) {
        HashSet<Integer> dnum=new HashSet<>();
        for(int n:nums){
            dnum.add(n);
        }
        int total=dnum.size();
        int count=0;
        for(int i=0;i<nums.length;i++){
            HashMap<Integer,Integer> fmap=new HashMap<>();
            int dcount=0;
            for(int j=i;j<nums.length;j++){
                fmap.put(nums[j],fmap.getOrDefault(nums[j],0)+1);
                if(fmap.get(nums[j])==1){
                    dcount++;
                }
                if(dcount==total){
                    count++;
                }
            }
        }
        return count;
    }
}