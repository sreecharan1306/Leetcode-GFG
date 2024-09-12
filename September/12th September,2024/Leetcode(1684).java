class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        HashMap<Character,Integer>mp=new HashMap<>();
        for(int i=0;i<allowed.length();i++){
            mp.put(allowed.charAt(i),1);
        }
        int ans=0;
        for(int i=0;i<words.length;i++){
            boolean flag=true;
            for(int j=0;j<words[i].length();j++){
                char ch=words[i].charAt(j);
                if(!mp.containsKey(ch)){
                    flag=false;
                    break;
                }
                    
            }
            if(flag) ans+=1;
        }
        return ans;
    }
}