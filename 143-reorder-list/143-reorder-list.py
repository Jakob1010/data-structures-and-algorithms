# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseList(head):
            prev = None
            current = head
            while current:
                next_ = current.next
                current.next = prev
                prev = current
                current = next_
            return prev
        
        # find middle of list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        # reverse second part of list
        second_part = slow.next
        slow.next = None
        second_part = reverseList(second_part)
        
        
        first_part = head
        while first_part and second_part:
            first_next = first_part.next
            second_next = second_part.next
            
            second_part.next = None
            first_part.next = second_part
            second_part.next = first_next
            
            first_part = first_next
            second_part = second_next
            
        return head