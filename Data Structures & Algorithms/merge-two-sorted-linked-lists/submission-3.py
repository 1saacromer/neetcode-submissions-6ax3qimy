# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        d = head 

        l1p = list1 
        l2p = list2 

        while l1p and l2p: 

            if l1p.val <= l2p.val: 
                d.next = l1p
                l1p = l1p.next 

            else: 
                d.next = l2p 
                l2p = l2p.next 
            d = d.next
        
        if not l1p and l2p: 
            d.next = l2p
        
        if not l2p and l1p: 
            d.next = l1p 
        
        return head.next
        



