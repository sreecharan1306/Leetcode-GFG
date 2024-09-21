class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return map(int,sorted(map(str,range(1,n+1))))