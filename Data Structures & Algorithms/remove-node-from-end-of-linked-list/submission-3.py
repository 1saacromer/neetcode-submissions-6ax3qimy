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

        # advance the fast pointer n positions into the array
        while fast and n: 
            fast = fast.next 
            n-=1 
        
    
        print(fast)
        print(slow.val)
        # pointer placement logic 
        while fast: 
            slow = slow.next 
            fast = fast.next
    
        # remove logic 
        new_next = slow.next.next
        old_next = slow.next 
        old_next.next = None 
        slow.next = new_next 
        
        return dummy.next
        


        