# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: 
            return None

        root_idx = inorder.index(preorder[0])
        in_l_sublist = inorder[0:root_idx] 
        in_r_sublist = inorder[root_idx + 1: ]
        pre_l_sublist = preorder[1:len(in_l_sublist)+1]
        pre_r_sublist = preorder[len(in_l_sublist)+1:]

        root = TreeNode(preorder[0])
        root.left = self.buildTree(pre_l_sublist, in_l_sublist)
        root.right = self.buildTree(pre_r_sublist, in_r_sublist)
        return root 
        