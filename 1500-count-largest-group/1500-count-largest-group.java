class Solution {
    public int countLargestGroup(int n) {
     HashMap<Integer,Integer>map=new HashMap<>();
     int max=0;
     int count=0;
     for(int i=1;i<=n;i++){
        int m=digitsum(i);
        map.put(m,map.getOrDefault(m,0)+1);
            max=Math.max(max,map.get(m));
     }
     for(int v:map.values()){
        if(v==max){
            count++;
        }
     } 
     return count;  
    }
    public int digitsum(int n){
        int sum=0;
        while(n>0){
            sum+=n%10;
            n/=10;
        }
        return sum;
    }
}