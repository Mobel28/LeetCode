class Solution {
    public char kthCharacter(int k) {
          int popCount = Integer.bitCount(k - 1);
         return (char) ('a' + (popCount % 26));

    }
}