# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ll1=ListNode(-1)
        ll2=ListNode(-1)
        lesser=ll1
        greater=ll2
        while head is not None:
            if head.val<x:
                lesser.next=head
                lesser=lesser.next
            else:
                greater.next=head
                greater=greater.next
            head=head.next
        greater.next=None
        lesser.next=ll2.next
        return ll1.next

        