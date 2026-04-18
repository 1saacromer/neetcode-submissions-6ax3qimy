# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        queue = deque()
        queue.append((root, 1))

        res = defaultdict(list)
        res[1].append(root.val)


        while queue: 
            p_node, level = queue.popleft() 
            level += 1
            l = p_node.left 
            r = p_node.right 

            if l:
                queue.append((l, level))
                res[level].append(l.val)
            if r:   
                queue.append((r, level))
                res[level].append(r.val)
            
        return list(res.values())
            
 
                
        