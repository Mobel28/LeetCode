class Solution {
    public int clumsy(int n) {
        int count=0;
        Stack<Integer> stack=new Stack<>();
        stack.push(n);
        for(int i=n-1;i>=1;i--){
            if(count==0){
                stack.push(stack.pop()*i);
            }
            else if(count==1){
                stack.push(stack.pop()/i);
            }
            else if(count==2){
                stack.push(i);
            }
            else{
                stack.push(-i);
            }
            count=(count+1)%4;
        }
        int result=0;
        for(int m:stack){
            result+=m;
        }
        return result;
    }
}