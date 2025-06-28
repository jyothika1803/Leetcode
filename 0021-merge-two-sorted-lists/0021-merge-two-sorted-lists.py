# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode(-1)
        new_head=temp
        while list1 is not None and list2 is not None:
            if list1.val<list2.val:
                new_head.next=list1
                list1=list1.next
            else:
                new_head.next=list2
                list2=list2.next
            new_head=new_head.next
        if list1 is not None:
            new_head.next=list1
        else:
            new_head.next=list2
        return temp.next
        