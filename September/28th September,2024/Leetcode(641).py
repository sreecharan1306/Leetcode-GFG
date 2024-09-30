class MyCircularDeque:

    def __init__(self, k: int):
        self.list=[-1]*k
        self.limit=k
        self.front=0
        self.rear=0
        self.cnt=0
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.list[self.front]=value    
        else:
            self.front=self.front-1
            self.front%=self.limit
            self.list[self.front]=value
        self.cnt+=1
        return True
        
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.list[self.front]=value
        else:
            self.rear=self.rear+1
            self.rear%=self.limit
            self.list[self.rear]=value
        self.cnt+=1
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.list[self.front]=-1
        self.front=self.front+1
        self.front%=self.limit
        self.cnt-=1
        if self.isEmpty():
            self.rear=self.front
        return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.list[self.rear]=-1
        self.rear=self.rear-1+self.limit
        self.rear%=self.limit
        self.cnt-=1
        if self.isEmpty():
            self.front = self.rear
        return True
        
    def getFront(self) -> int:
        # if self.isEmpty():
        #     return -1
        return self.list[self.front]

    def getRear(self) -> int:
        # if self.isEmpty():
        #     return -1
        return self.list[self.rear]
        

    def isEmpty(self) -> bool:
        return self.cnt==0
    
    def isFull(self) -> bool:
        return self.cnt==self.limit
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()