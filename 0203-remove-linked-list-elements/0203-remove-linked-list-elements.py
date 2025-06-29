# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp=ListNode(-1)
        new_head=temp
        while head is not None:
            if head.val !=val:
                new_head.next=head
                new_head=new_head.next
            head=head.next
        new_head.next=None
        return temp.next
