package October.22nd October,2024;

public // User function Template for Java

class Solution {

    static int sameOccurrence(int arr[], int x, int y) {
        // write code here
        HashMap<Integer,Integer>mp=new HashMap<>();
        int c=0;
        mp.put(0,1);
        int ans=0;
        for(int i:arr){
            if(i==x)++c;
            else if(i==y) --c;
            if(mp.containsKey(c)) ans+=mp.get(c);
            mp.put(c,mp.getOrDefault(c,0)+1);
        }
        return ans;
    }
} {
    
}
