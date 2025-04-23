class Solution {
    public String reversePrefix(String word, char ch) {
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == ch) {
                String prefix = word.substring(0, i + 1);
                StringBuilder reversed = new StringBuilder(prefix).reverse();
                return reversed.toString() + word.substring(i + 1);
            }
        }
        return word;
    }
}







