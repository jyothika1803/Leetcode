# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        dummyNode=head
        carry=0
        while l1 is not None or l2 is not None or carry>0:
            if l1 is not None:
                c1=l1.val
            else:
                c1=0
            if l2 is not None:
                c2=l2.val
            else:
                c2=0
            val=c1+c2+carry
            carry=val//10
            node_digit=val%10
            newNode=ListNode(node_digit)
            dummyNode.next=newNode
            dummyNode=dummyNode.next
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        return head.next
            






        