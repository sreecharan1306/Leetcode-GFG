class Solution:
    def compressedString(self, word: str) -> str:
        ans=""
        cnt=1
        char=word[0]
        for i in range(1,len(word)):
            if word[i]==char:
                cnt+=1
            else:
                p=cnt//9
                if p<0:
                    ans+=str(cnt)
                    ans+=char
                else:
                    for _ in range(p):
                        ans+=str(9)
                        ans+=char
                    if cnt%9 !=0:
                        ans+=str(cnt%9)
                        ans+=char
                char=word[i]
                cnt=1
        
        p=cnt//9
        if p<0:
            ans+=str(cnt)
            ans+=char
        else:
            for _ in range(p):
                ans+=str(9)
                ans+=char
            if cnt%9 !=0:
                ans+=str(cnt%9)
                ans+=char
        return ans