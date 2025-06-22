# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first = second = dummy
        for i in range(n + 1):
            second = second.next
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        return dummy.next
