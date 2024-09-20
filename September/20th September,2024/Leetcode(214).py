class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        # def ispal(s, l, r):
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True
        pref,suff=0,0
        mod=10**+7
        li=0
        r=s[::-1]
        base=26
        po=1
        for i in range(len(s)):
            char=(ord(s[i])-ord('a')+1)
            pref=(pref*base)%mod
            pref=(pref+char)%mod
            suff=(suff+char*po)%mod
            po=(po*base)%mod
            if pref==suff:
                li=i
                
                
        temp=s[li+1:]

        return temp[::-1]+s
