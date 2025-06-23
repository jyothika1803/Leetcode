# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if k==0:
            return head
        slow=head
        length=0
        curr=head
        while curr is not None: # count lenth of the list
            length+=1
            curr=curr.next
        k= k%length
        if k==0:
            return head
        fast=head
        while k>0:
            fast=fast.next
            k-=1
        while fast.next is not None:
            fast=fast.next
            slow=slow.next
    
        new_head=slow.next
        slow.next=None
        fast.next=head
        return new_head



        

        