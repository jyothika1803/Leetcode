# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptrA=headA
        ptrB=headB
        while ptrA != ptrB:
            if ptrA is not None:
                ptrA=ptrA.next
            else:
                ptrA=headB
            if ptrB is not None:
                ptrB=ptrB.next
            else:
                ptrB=headA
        return ptrA

        