class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rs = len(rowSum)
        cs = len(colSum)
        matrix = [[0] * cs for i in range(rs)]
        for i in range(rs):
            for j in range(cs):
                matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        return matrix
