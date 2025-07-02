class Solution {
    public int[] searchRange(int[] nums, int target) {
      int first=ffind(nums,target);
      int last=lfind(nums,target);
      return new int[]{first,last};
    }
    public int ffind(int[] nums,int target){
        int l=0;
        int r=nums.length-1;
        int res=-1;
        while(l<=r){
            int mid=l+(r-l)/2;
            if(nums[mid]==target){
                res=mid;
                r=mid-1;
            }
            else if(nums[mid]<target){
                l=mid+1;
            }
            else{
                r=mid-1;
            }
        }
        return res;
    }
    public int lfind(int[] nums,int target){
        int l=0;
        int r=nums.length-1;
        int res=-1;
        while(l<=r){
            int mid=l+(r-l)/2;
            if(nums[mid]==target){
                res=mid;
                l=mid+1;
            }
            else if(nums[mid]<target){
                l=mid+1;
            }
            else{
                r=mid-1;
            }
        }
        return res;
    }
}