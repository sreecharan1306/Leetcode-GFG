class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        n=len(prices)
        for i,e in enumerate(prices):
            # if i==n-1:
            #     ans.append(e)
            #     return ans
            for k in range(i+1,n):
                if prices[k]<=e:
                    ans.append(e-prices[k])
                    break
            else:
                ans.append(e)

        return ans