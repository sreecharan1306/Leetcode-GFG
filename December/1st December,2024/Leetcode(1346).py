class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s=set(arr)
        if arr.count(0)>1:
            return True
        for i in arr:
            if i!=0 and 2*i in arr:
                return True
        return False