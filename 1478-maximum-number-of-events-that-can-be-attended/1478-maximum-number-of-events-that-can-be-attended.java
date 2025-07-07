class Solution {
    public int maxEvents(int[][] events) {
        Arrays.sort(events,(a,b)->Integer.compare(a[0],b[0]));
        PriorityQueue<Integer> min=new PriorityQueue<>();
        int i=0;
        int n=events.length;
        int count=0;
        int last=0;
        for(int[] event:events){
            last=Math.max(last,event[1]);
        }
        for(int day=1;day<=last;day++){
            while(i<n && events[i][0]==day){
                min.offer(events[i][1]);
                i++;
            }
            while(!min.isEmpty()&&min.peek()<day){
                min.poll();
            }
            if(!min.isEmpty()){
                min.poll();
                count++;
            }
             if (i >= n && min.isEmpty()) {
                break;
            }
        }
        return count;
    }
}