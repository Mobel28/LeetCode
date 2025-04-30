class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int r=matrix.length;
        int c=matrix[0].length;
        int l=0;
        int h=r*c-1;
        while(l<=h){
            int m=l+(h-l)/2;
            int mv=matrix[m/c][m%c];
            if(mv==target)return true;
            else if(mv<target) l=m+1;
            else h=m-1;
        }
        return false;
    }
}