class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        p=sentence.split()
        for i in range(1,len(p)):
            if p[i-1][-1]!=p[i][0]:
                return False
        return p[-1][-1]==p[0][0]
