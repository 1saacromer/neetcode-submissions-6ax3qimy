"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node: 
            return node
        cpy = Node(node.val)
        seen = {}
        def dfs(n, nbrs): 

            for nbr in nbrs:
                if nbr.val not in seen: 
                    nn = Node(nbr.val)
                    seen[nbr.val] = nn 
                    n.neighbors.append(nn)
                    dfs(nn, nbr.neighbors) 
                else:
                    n.neighbors.append(seen[nbr.val])
            


        
        dfs(cpy, node.neighbors)

        return cpy
        

        


            
        