class Solution:
    def celebrity(self, mat):
        # code here
        ansl=[]
        for i in mat:
            if i.count(0)==len(i):
                ansl.append(mat.index(i))
        if len(ansl)==1:
            p=ansl[0]
            for i in mat:
                if i!=mat[p] and i[p]==0:
                    return -1
            return p
                    
        return -1


#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends