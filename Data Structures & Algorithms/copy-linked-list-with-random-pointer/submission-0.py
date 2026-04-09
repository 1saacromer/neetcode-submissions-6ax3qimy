"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        new = {} 
        curr = head 
        while curr: 
            new[curr] = Node(curr.val)
            curr = curr.next 
        
        curr = head
        while curr: 
            new[curr].next = new[curr.next] if new.get(curr.next) else None
            new[curr].random = new[curr.random] if new.get(curr.random) else None
            curr = curr.next
        

        return new[head] if new.get(head) else None


       



        