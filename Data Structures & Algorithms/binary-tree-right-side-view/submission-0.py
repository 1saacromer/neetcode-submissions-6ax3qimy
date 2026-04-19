# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [] 
        q = deque()
        q.append(root) 

        while q: 
            level = [] 
            qLen = len(q) 
            for _ in range(qLen): 
                n = q.popleft()
                if n: 
                    level.append(n.val)
                    q.append(n.left)
                    q.append(n.right)

            if level: 
                res.append(max(level))
        
        return res 