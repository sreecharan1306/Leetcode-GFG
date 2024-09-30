class CustomStack:

    def __init__(self, maxSize: int):
        self.list = []
        self.l = maxSize
        self.cnt = 0

    def push(self, x: int) -> None:
        if self.cnt<self.l:
            self.list.append(x)
            self.cnt+=1
        print("a", self.list, self.cnt)

    def pop(self) -> int:
        if self.cnt == 0:
            return -1
        ans = self.list[self.cnt-1]
        self.list.pop(self.cnt-1)
        self.cnt -= 1
        print("b", self.list, self.cnt)
        return ans

    def increment(self, k: int, val: int) -> None:
        if self.cnt < k:
            for i in range(self.cnt):
                self.list[i]+=val
        else:
            for i in range(0,k):
                self.list[i]+=val
        print("c", self.list, self.cnt)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
