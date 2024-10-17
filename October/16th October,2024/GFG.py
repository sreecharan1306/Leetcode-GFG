class Solution:
    def checkSorted(self, arr):
        #code here
        p=[i for i in range(1,len(arr)+1)]
        return arr==p or arr==p[::-1]
