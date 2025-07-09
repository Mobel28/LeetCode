class Solution {
    public int maxFreeTime(int eventTime, int k, int[] startTime, int[] endTime) {
     int n=endTime.length;
     ArrayList<Integer> gap=new ArrayList<>();
     gap.add(startTime[0]);
     for(int i=1;i<n;i++){
        gap.add(startTime[i]-endTime[i-1]);
     }  
     gap.add(eventTime-endTime[n-1]);
     int sum=0;
     for(int i=0;i<=k&&i<gap.size();i++){
        sum+=gap.get(i);
     }
     int maxsum=sum;
     for(int i=k+1;i<gap.size();i++){
        sum+=gap.get(i)-gap.get(i-(k+1));
        maxsum=Math.max(sum,maxsum);
     }
     return maxsum;
    }
}