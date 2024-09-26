class MyCalendar:
    
    def __init__(self):
        self.cal=[]

    def book(self, start: int, end: int) -> bool:
        for s,e in self.cal:
            if not (e<=start or end<=s):
                return False
        self.cal.append((start,end))
        return True
            
    # def search(self,l,h):
    #     while l<=h:
    #         m=(l+h)//2
    #         if m in self.cal:
    #             return False
    #         else:
    #             return self.search(l,m-1) and self.search(m+1,h)
    #     return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)