class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        int[][] ans=new int[m][n];
        int s=original.length;
        if((m*n)!=s) return new int[0][0];
        for(int i=0;i<s;i++){
            ans[i/n][i%n]=original[i];
        }
        return ans;

    }
}