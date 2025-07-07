class ListNode:
    def __init__(self,val=0):
        self.val=val
        self.next=None

class MyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    
    def get(self,index:int)->int:
        if index<0 or index>=self.size:
            return -1
        curr=self.head
        for i in range(index):
            curr=curr.next
        return curr.val
    
    def addAtHead(self,val:int)->None:
        new_node=ListNode(val)
        new_node.next=self.head
        self.head=new_node
        self.size+=1
    
    def addAtTail(self,val:int)->None:
        new_node=ListNode(val)
        if not self.head:
            self.head=new_node
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_node
        self.size+=1
    
    def addAtIndex(self,index:int,val:int)->None:
        if index<0 or index>self.size:
            return
        if index==0:
            self.addAtHead(val)
            return
        
        new_node=ListNode(val)
        curr=self.head
        for i in range(index-1):
            curr=curr.next
        new_node.next=curr.next
        curr.next=new_node
        self.size+=1
    
    def deleteAtIndex(self,index:int)->None:
        if index<0 or index>=self.size:
            return
        if index==0:
            self.head=self.head.next
        else:
            curr=self.head
            for i in range(index-1):
                curr=curr.next
            curr.next=curr.next.next
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)