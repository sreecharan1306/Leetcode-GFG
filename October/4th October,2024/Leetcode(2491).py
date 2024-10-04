class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)
        i,j=0,n-1
        t=skill[0]+skill[-1]
        temp=[]
        print(skill)
        while i<=j:
            if skill[i]+skill[j]==t:
                temp.append([skill[i],skill[j]])
                i+=1
                j-=1
            else:
                return -1
        temp=map(lambda x:x[0]*x[1],temp)
        return sum(temp)