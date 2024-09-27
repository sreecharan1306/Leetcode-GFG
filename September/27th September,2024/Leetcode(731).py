class MyCalendarTwo:

    def __init__(self):
        self.ol=[]
        self.nol=[]
        

    def book(self, start: int, end: int) -> bool:
        for s,e in self.ol:
            if e>start and s<end:
                return False
        
        for s,e in self.nol:
            if e>start and s<end:
                self.ol.append((max(s,start),min(e,end)))

        
        self.nol.append((start,end))        
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)