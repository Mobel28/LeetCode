class Solution {
    private static final String vowel="aeiouAEIOU";
    public boolean isValid(String word) {
        if(word.length()<3)return false;
        int v=0, c=0;
        for(char ch:word.toCharArray()){
            if(Character.isDigit(ch))continue;
            if(Character.isLetter(ch)){
                if(vowel.indexOf(ch)>=0)v++;
                else c++;
            }
            else{
                return false;
            }
        }
        return v>0&&c>0;
    }
}