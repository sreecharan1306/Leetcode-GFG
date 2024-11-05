#User function Template for python3

def rotate(matrix): 
    #code here
    n=len(matrix)
    for i in range(n):
        for j in range(n):
            if i<j:
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in matrix:
        i.reverse()

    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        matrix = []
        for i in range(N):
            arr = [int(x) for x in input().strip().split()]
            matrix.append(arr)

        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()
        print("~")

# } Driver Code Ends