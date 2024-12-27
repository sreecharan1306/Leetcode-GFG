class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int n=values.length;
        int ans=Integer.MIN_VALUE;
        int ms=values[0];
        for(int i=1;i<n;i++){
            ans=Math.max(ms+values[i]-i,ans);
            ms=Math.max(ms,values[i]+i);
        }
        return ans;

    }
}