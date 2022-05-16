# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        offset = 0
        dummy = ListNode(0)
        current = dummy
        
        while l1 or l2:
            if l1 and not l2:
                offset += l1.val
                l1 = l1.next
            elif l2 and not l1:
                offset += l2.val
                l2 = l2.next
            else:
                offset += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            current.next = ListNode(offset % 10)
            current = current.next
            offset = offset // 10
        if offset != 0:
            current.next = ListNode(offset)
        
        return dummy.next