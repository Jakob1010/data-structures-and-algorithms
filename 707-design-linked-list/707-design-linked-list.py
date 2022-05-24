class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        current = self.head
        for i in range(index+1):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return -1
        
        current = self.head
        for i in range(index):
            current = current.next
        old_at_index = current.next
        current.next = ListNode(val,old_at_index)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return -1
        
        current = self.head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1
       