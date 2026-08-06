# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node, curr_path):
            if not node:
                return
            curr_path.append(str(node.val))
            if not node.left and not node.right:
                cu = "".join(curr_path)
                res.append(int(cu))
                curr_path.pop()
                return
            else:
                dfs(node.left, curr_path)
                dfs(node.right, curr_path)
            
            curr_path.pop()
        
        dfs(root, [])
        return sum(res)