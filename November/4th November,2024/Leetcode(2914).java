public class Solution {
    public int minChanges(String s) {
        int n=s.length(),c=0;
        for(int i=1;i<n;i+=2) if(s.charAt(i)==s.charAt(i-1)) c+=2;
        return (n-c)/2;
    }
} Leetcode(2914) {
    
}
