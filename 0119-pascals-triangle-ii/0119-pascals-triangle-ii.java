class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res=new ArrayList<>();
        res.add(1);
        for(int i=1;i<=rowIndex;i++){
            List<Integer> rset=new ArrayList<>();
            rset.add(1);
            for(int j=1;j<i;j++){
                rset.add(res.get(j-1)+res.get(j));
            }
            rset.add(1);
            res=rset;
        }
        return res;
    }
}