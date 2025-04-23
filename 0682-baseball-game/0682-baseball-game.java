class Solution {
    public int calPoints(String[] operations) {
        ArrayList<Integer> rec=new ArrayList<>();
        for(int i=0;i<operations.length;i++){
            int size=rec.size();
            String op=operations[i];
            if(op.equals("C")){
                rec.remove(size-1);
            }
            else if(op.equals("D")){
                rec.add(rec.get(size-1)*2);
            }
            else if(operations[i].equals("+")){
                rec.add(rec.get(size-1)+rec.get(size-2));
            }
            else{
                rec.add(Integer.parseInt(op));
            }
        }
        int sum=0;
        for(int n:rec){
            sum+=n;
        }
        return sum;
    }
}