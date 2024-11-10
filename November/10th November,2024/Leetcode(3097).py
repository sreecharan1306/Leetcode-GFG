class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        p = 0
        for i in nums:
            p |= i
        if p < k:
            return -1
        res = 1000000
        n = len(nums)
        if k == 0:
            return 1
        bits = [0] * 32

        def incdec(bits, n, d):
            for i in range(32):
                if n & (1 << i):
                    bits[i] += d

        def val(bits):
            ans = 0
            for i in range(32):
                if bits[i]:
                    ans += 1 << i
            return ans

        i = 0
        for j in range(n):
            incdec(bits, nums[j], 1)
            c = val(bits)
            # res = min(res, j - i + 1)
            while i <= j and c >= k:
                res = min(res, j - i + 1)
                incdec(bits, nums[i], -1)
                c = val(bits)
                i += 1

        return res