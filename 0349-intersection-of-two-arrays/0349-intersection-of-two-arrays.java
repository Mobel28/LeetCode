class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set <Integer> set=new HashSet<>();
        Set<Integer> rset=new HashSet<>();
        for(int n:nums1){
            set.add(n);
        }
        for(int n:nums2){
            if(set.contains(n)){
                rset.add(n);
            }
        }
        int[] result=new int[rset.size()];
        int i=0;
        for(int n:rset){
            result[i]=n;
            i++;
        }
        return result;
    }
}