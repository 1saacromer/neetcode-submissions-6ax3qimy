# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head 

        while fast and n: 
            fast = fast.next 
            n-=1 
        
    
        while fast: 
            slow = slow.next 
            fast = fast.next
    
        new_next = slow.next.next
        old_next = slow.next 
        old_next.next = None 
        slow.next = new_next 
        
        return dummy.next
        


        