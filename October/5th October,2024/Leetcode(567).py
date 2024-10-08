from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s=set(permutations(s1))
        p=Counter(s1)
        
        # print(p)
        n1=len(s1)
        n2=len(s2)
        i,j=0,n1-1
        while j<n2:
            if Counter(s2[i:j+1])==p:
                return True
            # print(Counter(s2[i:j+1]))
            i+=1
            j+=1
            
        return False