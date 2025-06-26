# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        while head is not None:
            curr=head.next
            head.next=prev
            prev=head
            head=curr
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rl1=self.reverseList(l1)
        rl2=self.reverseList(l2)
        carry=0
        result=ListNode(-1)
        curr=result
        while rl1 is not None or rl2 is not None or carry!=0:
            if rl1 is not None:
                val1=rl1.val
            else:
                val1=0
            if rl2 is not None:
                val2=rl2.val
            else:
                val2=0
            total=val1+val2+carry
            carry=total//10
            curr.next=ListNode(total%10)
            curr=curr.next
            if rl1 is not None:
                rl1=rl1.next
            if rl2 is not None:
                rl2=rl2.next
        return self.reverseList(result.next)
            

