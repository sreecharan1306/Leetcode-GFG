# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=set(nums)
        while head.val in s:
            head=head.next
        temp=head
        bs=head.next
        while bs:
            if bs.val not in s:
                temp.next=bs
                temp=temp.next
            bs=bs.next
        temp.next=None
        return head