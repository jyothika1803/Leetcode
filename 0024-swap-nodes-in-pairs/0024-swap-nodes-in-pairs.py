# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev=None
        ptr=head
        while ptr is not None and ptr.next is not None:
            curr=ptr.next
            ptr.next=curr.next
            curr.next=ptr

            if prev is None:
                head=curr
            else:
                prev.next=curr
            prev=ptr
            ptr=ptr.next
        return head
        