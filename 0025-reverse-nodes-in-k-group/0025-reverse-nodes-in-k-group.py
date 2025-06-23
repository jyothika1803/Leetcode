# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_k_nodes(head,tail):
            ptr=head
            head=tail
            while ptr != tail:
                curr=ptr.next
                ptr.next=head
                head=ptr
                ptr=curr
            return head    
        if head is None or head.next is None or k==1:
            return head
        ptr=head
        new_head=None
        prev=None
        count=0
        while ptr is not None or count==k:
            if count<k:
                count+=1
                ptr=ptr.next
            else:
                count=0
                node=reverse_k_nodes(head,ptr)
                if new_head is None:
                    new_head=node
                    prev=head
                    head=ptr
                else:
                    prev.next=node
                    prev=head
                    head=ptr
        return new_head
