class Solution {
    public String minWindow(String s, String t) {
      if(s.length()<t.length()||s==null||t==null)return "";  
      HashMap <Character,Integer> need=new HashMap<>();
      for(char c:t.toCharArray()){
        need.put(c,need.getOrDefault(c,0)+1);
      }
      HashMap<Character,Integer> window=new HashMap<>();
      int r=0,l=0,strt=0,valid=0,min=Integer.MAX_VALUE;
      while(r<s.length()){
        char ch=s.charAt(r);
        r++;
        if(need.containsKey(ch)){
            window.put(ch,window.getOrDefault(ch,0)+1);
            if(window.get(ch).intValue()==need.get(ch).intValue()){
                valid++;
            }
        }
        while(valid==need.size()){
            if(r-l<min){
                min=r-l;
                strt=l;
            }
            char re=s.charAt(l);
            l++;
            if(need.containsKey(re)){
                if(window.get(re).intValue()==need.get(re).intValue()){
                    valid--;
                }
                window.put(re,window.get(re)-1);
            }
        }
      }
      return min==Integer.MAX_VALUE?"":s.substring(strt,min+strt);
    }
}
