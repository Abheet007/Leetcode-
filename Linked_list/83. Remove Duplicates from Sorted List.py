# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        c = p.next
        while c:
            if p.val==c.val:
                p.next = c.next
            else:
                p = c
            c = c.next
        return head
            
        
        
        
        
        
