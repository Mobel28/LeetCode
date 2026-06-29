class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int count=0;
        for (int i=0;i<patterns.length;i+=1){
            Boolean found=false;
            String cWord=patterns[i];
            for (int start=0;start<word.length() && !found;start+=1){
                String temp="";
                temp+=word.charAt(start);
                if (temp.equals(cWord)){
                    count+=1;
                    found=true;
                }
                for(int end=start+1;end<word.length();end+=1){

                    temp+=word.charAt(end);
                    if (temp.equals(cWord)){
                        found=true;
                        System.out.println(temp);
                        count+=1;
                        break;
                    }
                    else{
                        continue;
                    }
                }
            }
        }
        return count;
    }
}

//TC=O(N^2)
//SC=O(1)