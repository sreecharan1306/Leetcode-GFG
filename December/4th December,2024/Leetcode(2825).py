class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i,j=0,0
        l1=len(str1)
        l2=len(str2)
        while i<l1 and j<l2:
            if str1[i]==str2[j] or (str1[i]=='z' and str2[j]=='a') or (ord(str1[i])+1 == ord(str2[j])):
                i+=1
                j+=1

            else:
                i+=1

        return j==l2