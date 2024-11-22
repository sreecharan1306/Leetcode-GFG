class Solution {
    void helper(int r,int c,int m,int n,int mat[][]){
        int l[]={1,0,-1,0};
        int q[]={0,1,0,-1};
        for(int i=0;i<4;i++){
            int nr=r+l[i];
            int nc=c+q[i];
            while(nr>=0 && nr<m && nc>=0 && nc<n ){
                if(mat[nr][nc]==1 || mat[nr][nc]==2) break;
                mat[nr][nc]=3;
                nr+=l[i];
                nc+=q[i];
            }
        }
        return;
    }
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int mat[][]=new int[m][n];
        for (int i=0;i<walls.length;i++) {
            int r = walls[i][0];
            int c = walls[i][1];
            mat[r][c] = 1;
        }
        for (int i=0;i<guards.length;i++) {
            int r = guards[i][0];
            int c = guards[i][1];
            mat[r][c] = 2;
        }
        for (int i=0;i<guards.length;i++) {
            int r = guards[i][0];
            int c = guards[i][1];
            helper(r,c,m,n,mat);
        }
        int ans=0;
        for (int i=0;i<m;i++) for (int j=0;j<n;j++) if(mat[i][j]==0) ans++;
        return ans;
    }
}