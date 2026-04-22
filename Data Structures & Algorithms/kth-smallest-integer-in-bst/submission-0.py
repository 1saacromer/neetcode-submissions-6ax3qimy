# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        inOrder = [] 

        self.inOrder(root, inOrder)

        return inOrder[k-1]

    
    def inOrder(self, root, res): 

        if not root: 
            return 

        self.inOrder(root.left, res)

        res.append(root.val) 

        self.inOrder(root.right, res)



        