# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        dummy = ListNode(-1)
        sorted_list = dummy
        
        for i,l in enumerate(lists):
            if l:
                heapq.heappush(q,(l.val,i))
            
        while q:
            current_val, current_i = heapq.heappop(q)
            sorted_list.next = ListNode(current_val)
            sorted_list = sorted_list.next
            if lists[current_i].next:
                lists[current_i] = lists[current_i].next
                heapq.heappush(q,(lists[current_i].val,current_i))
        
        return dummy.next
        