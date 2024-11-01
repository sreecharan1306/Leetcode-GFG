#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
    #code here
        temp=head
        nn=Node(x)
        if not head:
            return nn
        
        if x<=head.data:
            nn.next=head
            head.prev=nn
            return nn
        p=None
        while temp and x>temp.data:
            p=temp
            temp=temp.next
        # print(p.data)
        # if x<temp.data:
        if temp:
            p.next=nn
            nn.next=temp
            temp.prev=nn
            nn.prev=p
        else:
            p.next=nn
            nn.prev=p

        return head


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        values = list(map(int, input().strip().split()))
        head = None
        tail = None

        for value in values:
            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        value_to_insert = int(input().strip())
        solution = Solution()
        head = solution.sortedInsert(head, value_to_insert)
        print_list(head)

        print("~")

# } Driver Code Ends