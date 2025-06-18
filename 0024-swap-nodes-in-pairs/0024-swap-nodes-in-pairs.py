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
        while ptr and ptr.next:
            temp=ptr.next
            ptr.next=temp.next
            temp.next=ptr
            if prev:
                prev.next=temp
            else:
                head=temp
      
            prev=ptr
            ptr=ptr.next
        return head
        
        