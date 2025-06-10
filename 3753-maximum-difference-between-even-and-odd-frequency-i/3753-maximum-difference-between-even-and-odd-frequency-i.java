class Solution {
    public int maxDifference(String s) {
        int ocount=Integer.MIN_VALUE;
        int ecount=Integer.MAX_VALUE;
        Map<Character,Integer> map=new HashMap<>();
        for(char c:s.toCharArray()){
            map.put(c,map.getOrDefault(c,0)+1);  
        }
        for(int c:map.values()){
            if(c%2==0){
                ecount=Math.min(ecount,c);
            }
            else{
                ocount=Math.max(ocount,c);
            }
        }
        return ocount-ecount;
    }
}