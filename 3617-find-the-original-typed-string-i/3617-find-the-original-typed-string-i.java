class Solution {
    public int possibleStringCount(String word) {
      int c=0;
      for(int i=1;i<word.length();i++){
        if(word.charAt(i)==word.charAt(i-1)){
            c++;
        }
      }  
      return c+1;
    }
}