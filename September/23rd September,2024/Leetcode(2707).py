class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dictionary.sort(key=lambda x:len(x),reverse=True)
        se = set(dictionary)
        dp={len(s):0}
        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1)

            for j in range(i, len(s)):
                if s[i : j + 1] in se:
                    res = min(res, dfs(j + 1))
            dp[i]=res
            return res

        return dfs(0)
