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
        new = collections.defaultdict(lambda: Node(0))
        new[None] = None 

        curr = head
        while curr: 
            new[curr].val = curr.val 
            new[curr].next = new[curr.next]
            new[curr].random = new[curr.random] 
            curr = curr.next 
        
        return new[head]

       



        