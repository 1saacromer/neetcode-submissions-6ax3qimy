# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        p1, p2, c, head = l1, l2, 0, dummy
        while p1 or p2 or c: 
            p1v = p1.val if p1 else 0 
            p2v = p2.val if p2 else 0 

            psum = (p1v + p2v + c) % 10 
            c = (p1v + p2v + c) // 10  

            head.next = ListNode(psum) 
             
            p1 = p1.next if p1 else None 
            p2 = p2.next if p2 else None 
            head = head.next 



        


        return dummy.next 
        

        