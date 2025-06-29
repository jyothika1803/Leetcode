# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_odd=ListNode(-1)
        odd=temp_odd
        temp_even=ListNode(-1)
        even=temp_even
        curr=head
        index=1
        while curr is not None:
            if index%2==0:
                even.next=curr
                even=even.next
            else:
                odd.next=curr
                odd=odd.next
            curr=curr.next
            index+=1
        even.next=None
        odd.next=temp_even.next
        return temp_odd.next
