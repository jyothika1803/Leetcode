# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyNode1=ListNode(0)
        dummyNode2=ListNode(0)
        current1=dummyNode1
        current2=dummyNode2
        current=head
        while current:
            if current.val<x:
                current1.next=current
                current1=current1.next
            else:
                current2.next=current
                current2=current2.next
            current=current.next
        current2.next=None
        current1.next=dummyNode2.next
        return dummyNode1.next


        