#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        m=len(mat)
        n=len(mat[0])
        q=[]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append([i,j])
        for a,b in q:
            for i in range(m):
                mat[i][b]=0
            for i in range(n):
                mat[a][i]=0
        return mat
