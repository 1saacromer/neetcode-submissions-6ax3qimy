# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0 
        currMax = -101

        return self.dfs(root, currMax)

    def dfs(self, root: TreeNode, currMax: int) -> int:
        res = 0

        # None values contribute no extra counts
        if not root: 
            return res
        
        # value condition  
        if root.val >= currMax: 
            res += 1
        
        currMax = max(root.val, currMax)

        res += self.dfs(root.right, currMax)
        res += self.dfs(root.left, currMax) 

        return res
        

        

        
    

        