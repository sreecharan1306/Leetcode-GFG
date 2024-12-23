class Solution:
    def bs(self, h, st):
        l, r = 0, len(st) - 1
        a = -1
        while l <= r:
            m = (l + r) // 2
            if st[m][0] > h:
                a = m
                l = m + 1
            else:
                r = m - 1
        return a

    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        # def bs(h, st):
        #     l, r = 0, len(st) - 1
        #     a = -1
        #     while l <= r:
        #         m = (l + r) // 2
        #         if st[m][0] > h:
        #             a = m
        #             l = m + 1
        #         else:
        #             r = m - 1
        #     return ans

        n = len(heights)
        n1 = len(queries)
        ans = [-1] * n1
        st = []
        nq = [[] for _ in range(n)]
        for i, e in enumerate(queries):
            a, b = e
            if a > b:
                a, b = b, a
            if heights[b] > heights[a] or a == b:
                ans[i] = b
            else:
                ans[i] = -1
            if ans[i]==-1:
                nq[b].append((heights[a], i))
        for i in range(n - 1, -1, -1):
            for h, idx in nq[i]:
                p = self.bs(h, st)
                if p != -1:
                    ans[idx] = st[p][1]
            while st and st[-1][0] <= heights[i]:
                st.pop()
            st.append((heights[i], i))
        return ans
