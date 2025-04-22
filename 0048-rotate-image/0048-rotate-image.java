class Solution {
    public void rotate(int[][] matrix) {
       int n=matrix.length;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int temp=matrix[j][i];
                matrix[j][i]=matrix[i][j];
                matrix[i][j]=temp;
            }
        }
        for(int i=0;i<n;i++){
            int l=0;
            int r=n-1;
            while(l<r){
                int temp=matrix[i][r];
                matrix[i][r]=matrix[i][l];
                matrix[i][l]=temp;
                l++;
                r--;
            }
        }
    }
}