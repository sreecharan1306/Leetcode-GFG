
#User function Template for python3

class Solution:
    def bs (self,arr,n,x):
        low =0
        high = n-1
        while low <= high :
            mid = (low +high )//2
            
            if arr[mid] == x:
                return True
            elif arr[mid] < x:
                low = mid +1
            else:
                high = mid -1
        return False
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
        # code here 
        for i in mat:
            if self.bs(i,len(i),x):
                return True
        return False
        

