# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode], interval: tuple) -> bool: 
            if not root: 
                return True 

            if root.val <= interval[0] or root.val >= interval[1]: 
                return False 

            li = (interval[0], root.val)
            ri = (root.val, interval[1])

            return dfs(root.left, li) and dfs(root.right, ri)






        return dfs(root, (-1001, 1001))











        