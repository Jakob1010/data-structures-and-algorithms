# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        mem = set()
        mem.add(headA)
        if headB in mem:
            return headB
        else:
            mem.add(headB)
        
        
        while headA or headB:
            if headA:
                headA = headA.next
                if headA in mem:
                    return headA
                else:
                    mem.add(headA)
                
            if headB:
                headB = headB.next
                if headB in mem:
                    return headB
                else:
                    mem.add(headB)
            
            mem.add(headB)
            
        return None