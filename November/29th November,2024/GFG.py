#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
	   # if len(s1)>len(s2):
	   #     return self.addBinary(s2,s1)
		# code here
		s1=s1.lstrip('0')
		s2=s2.lstrip('0')
        if not s1:
            return s2 if s2 else "0"
        if not s2:
            return s1 if s1 else "0"
		i, j = len(s1) - 1, len(s2) - 1
        car = 0
        res = []
        
        # Add the binary strings
        while i >= 0 or j >= 0 or car:
            d1 = int(s1[i]) if i >= 0 else 0
            d2 = int(s2[j]) if j >= 0 else 0
            
            # Compute the sum and the carry
            total = d1 + d2 + car
            car = total // 2
            res.append(str(total % 2))
            
            # Move the pointers
            i -= 1
            j -= 1
        return ''.join(res[::-1])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends