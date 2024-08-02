class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        # code here
        n=len(matrix)
        m=len(matrix[0])
        cb,ce=0,m
        rb,re=0,n
        res=[]
        while rb<re and cb<ce:
            for i in range(cb,ce):
                res.append(matrix[rb][i])
            rb+=1
            for i in range(rb,re):
                res.append(matrix[i][ce-1])
            ce-=1
            if rb<re:
                for i in range(ce-1,cb-1,-1):
                    res.append(matrix[re-1][i])
                re-=1
            if cb<ce:
                for i in range(re-1,rb-1,-1):
                    res.append(matrix[i][cb])
                cb+=1
        return res
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))

# } Driver Code Ends