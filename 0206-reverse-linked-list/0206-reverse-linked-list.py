# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=head
        prev=None
        while ptr is not None:
            curr=ptr.next
            ptr.next=prev
            prev=ptr
            ptr=curr
        return prev
        