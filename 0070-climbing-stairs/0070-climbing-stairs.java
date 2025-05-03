class Solution {
    public int climbStairs(int n) {
      if(n==1){
        return n;
      }
    int f=1,s=2;
    for(int i=2;i<n;i++){
        int t=f+s;
        f=s;
        s=t;
    }
    return s;
    }
}