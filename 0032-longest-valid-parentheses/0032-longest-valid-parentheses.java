class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stack=new Stack<>();
        int count=0;
        stack.push(-1);
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='('){
                stack.push(i);
            }
            else{
                stack.pop();
                if(stack.isEmpty()){
                    stack.push(i);
                }
                else{
                    count=Math.max(count,i-stack.peek());
                }
            }
        }
        return count;
    }
}