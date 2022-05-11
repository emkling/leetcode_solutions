# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        direction = 1
        result = []
        q = deque()
        q.append(root)
        
        while q:
            level = []
            
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                        
                    if node.right:
                        q.append(node.right)
                    
            if direction % 2 == 0:
                result.append(level[::-1])
            else:
                result.append(level[::1])
            direction += 1
            
            
        return result
    
    
    
    