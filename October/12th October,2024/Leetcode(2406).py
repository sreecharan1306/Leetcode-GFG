class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        ans = 0
        n = len(intervals)
        st = [i[0] for i in intervals]
        end = [i[1] for i in intervals]
        end.sort()
        k = intervals[0][1]
        i, j = 0, 0
        while i < n and j < n:
            if st[i] <= end[j]:
                i += 1
            else:
                j += 1
            ans = max(ans, i - j)
        return ans
