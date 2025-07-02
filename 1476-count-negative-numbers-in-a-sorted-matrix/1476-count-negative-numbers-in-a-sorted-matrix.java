class Solution {
    public int countNegatives(int[][] grid) {
        int rs=grid.length;
        int cs=grid[0].length;
        int count=0;
        for(int i=0;i<rs;i++){
            for(int j=0;j<cs;j++){
                if(grid[i][j]<0){
                    count++;
                }
            }
        }
        return count;
    }
}