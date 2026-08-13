# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        length = 0
        curr = head
        while curr: 
            length += 1 
            curr = curr.next
        
        half = length // 2 

        sever = head 
        count = 0
        
        head2 = None

        while count < half - 1: 
            sever = sever.next 
            count += 1
        
        head2 = sever.next 
        sever.next = None

        prev = None 
        curr = head2
        while curr: 
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        head2 = prev 

        result = ListNode() 
        d = result

        h1 = head 
        h2 = head2 

        while h1 and h2: 
            d.next = h1
            h1 = h1.next
            d.next.next = h2 
            h2 = h2.next
            d = d.next.next

        if not h2: 
            d.next = h2 
        
        head = result.next

            
        
        

        


        