class Solution {
    public int findLengthOfShortestSubarray(int[] arr) {
        int l=0;
        while(l+1<arr.length && arr[l]<=arr[l+1]){
            l++;
        }
        if(l==arr.length-1)return 0;
        int r=arr.length-1;
        while(r-1>=0 && arr[r]>=arr[r-1]){
            r--;
        }
        int minl=Math.min(arr.length-l-1,r);
        int i=0;
        int j=r;
        while(i<=l &&j<arr.length){
            if(arr[i]<=arr[j]){
                minl=Math.min(minl,j-i-1);
                i++;
            }
            else{
                j++;
            }
        }
        return minl;
    }
}