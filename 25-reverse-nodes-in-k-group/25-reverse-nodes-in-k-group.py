# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseGroup(self,head):
        prev = None
        current = head
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        current = dummy
        
        while current:
            # reverse from current.next to current.next + k - 1
            one_before = current
            start = current.next
            for i in range(k):
                if current:
                    current = current.next
            
            
            if current:
                one_after = current.next
                # remove group from list
                current.next = None
                self.reverseGroup(one_before.next)
                one_before.next = current
                start.next = one_after
                current = start
            else:
                break
            
            
        
        return dummy.next
            