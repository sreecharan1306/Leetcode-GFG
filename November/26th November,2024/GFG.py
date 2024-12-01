#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    def ms(arr,n):
        x=arr
        s=0
        p=s
        for i in x:
            s+=i
            if s>0:
                s=0
            p=min(s,p)
        return p
    ##Your code here
    s=0
    m=0
    for i in arr:
        s+=i
        if s<0:
            s=0
        m=max(s,m)
    return max(sum(arr)-ms(arr,len(arr)),m)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends