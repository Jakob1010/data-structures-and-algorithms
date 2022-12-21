# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n_a = 0
        n_b = 0
        a = headA
        b = headB
        
        while a or b:
            if a:
                n_a+=1
                a = a.next
            if b:
                n_b += 1
                b = b.next
                
        a = headA
        b = headB
        
        while a and b:
            if n_a > n_b:
                n_a -= 1
                a = a.next
            elif n_b > n_a:
                n_b -= 1
                b = b.next
            elif a == b:
                return a
            else:
                a = a.next
                b = b.next
        