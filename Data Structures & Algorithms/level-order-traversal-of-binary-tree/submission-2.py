# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# This approach allows None values on the Queue
# the solution elegantly process None values by either return an empty list if the root is empty 
# or ignoring empty level list down the line for None values that aren't the root 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque() 
        q.append(root) 

        while q: 
            qLen = len(q)
            level = [] 

            for i in range(qLen): 
                pNode = q.popleft()
                if pNode: 
                    q.append(pNode.left)
                    q.append(pNode.right)
                    level.append(pNode.val)
               
            if level: 
                res.append(level)
        
        return res 

            
 
                
        