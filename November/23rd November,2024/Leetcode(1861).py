class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m=len(box)
        n=len(box[0])
        ans=[["."] * m for _ in range(n)]

        for i in range(m):
            p=n-1
            for j in reversed(range(n)):
                if box[i][j]=="#":
                    ans[p][m-i-1]="#"
                    p-=1
                elif box[i][j]=="*":
                    ans[j][m-i-1]="*"
                    p=j-1
        return ans
