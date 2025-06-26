# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        result=ListNode(-1)
        curr=result
        while l1 is not None or l2 is not None or carry!=0:
            if l1 is not None:
                val1=l1.val
            else:
                val1=0
            if l2 is not None:
                val2=l2.val
            else:
                val2=0
            total=val1+val2+carry
            carry=total//10
            curr.next=ListNode(total%10)
            curr=curr.next
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        return result.next
            






        