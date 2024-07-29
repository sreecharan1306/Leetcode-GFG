class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minele=set()
        n=len(matrix)
        m=len(matrix[0])
        for i in matrix:
            minele.add(min(i))
        maxel=[-1]*m
        
        for i in range(n):
            for j in range(m):
                maxel[j]=max(maxel[j],matrix[i][j])
        maxele=set(maxel)
        
        return minele.intersection(maxele)