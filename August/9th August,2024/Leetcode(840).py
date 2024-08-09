class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, col = len(grid), len(grid[0])

        def solve(r, c):
            dup = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] in dup or not (1 <= grid[i][j] <= 9):
                        return 0
                    dup.add(grid[i][j])

            for i in range(r, r + 3):
                if sum(grid[i][c : c + 3]) != 15:
                    return 0

            for i in range(c, c + 3):
                if (grid[r][i] + grid[r + 1][i] + grid[r + 2][i]) != 15:
                    return 0

            if (
            grid[r+1][c+1]+grid[r][c]+grid[r+2][c+2]!=15 or
            grid[r+1][c+1]+grid[r+2][c]+grid[r][c+2]!=15
            ):
                return 0
            return 1
        res = 0
        for r in range(rows-2):
            for c in range(col-2):
                res+=solve(r,c)
        return res
