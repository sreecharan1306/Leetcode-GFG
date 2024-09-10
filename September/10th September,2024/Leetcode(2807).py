# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import *
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head.next
        curr=head
        if head.next is None:
            return head
        while temp:
            x=gcd(temp.val,curr.val)
            p=ListNode(x,temp)
            curr.next=p
            curr=temp
            temp=temp.next
        return head