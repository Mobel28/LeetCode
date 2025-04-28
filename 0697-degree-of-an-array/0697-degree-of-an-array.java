class Solution {
    public int findShortestSubArray(int[] nums) {
        HashMap<Integer,Integer> count=new HashMap<>();
        HashMap<Integer,Integer> first=new HashMap<>();
        HashMap<Integer,Integer> last=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            count.put(nums[i],count.getOrDefault(nums[i],0)+1);
            if(!first.containsKey(nums[i])){
                first.put(nums[i],i);
            }
            last.put(nums[i],i);
        }
        int degree=Integer.MIN_VALUE;
        for(int k:count.keySet()){
            degree=Math.max(degree,count.get(k));
        }
        int min=Integer.MAX_VALUE;
        for(int k:count.keySet()){
            if(degree==count.get(k)){
                min=Math.min(min,last.get(k)-first.get(k)+1);
            }
        }
        return min;
    }
}