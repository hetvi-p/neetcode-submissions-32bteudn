# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        h1 = head
        
        while (head):
                        
            if head.next is None:
                return False

            if head.next == -1:
                return True

            h1 = head.next
            head.next = -1
            head = h1
            
        return False
            
        