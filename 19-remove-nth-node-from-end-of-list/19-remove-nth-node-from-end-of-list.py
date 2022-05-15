# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        
        # get length of list
        while current:
            length+=1
            current = current.next
        # if n is greater then length of list
        # cut overhead
        if n > length:
            n = n - length * (n//length)
        if n == length:
            return head.next
        
        current = head
        for i in range(length-n-1):
            current = current.next
            
        current.next = current.next.next
        return head