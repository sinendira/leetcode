# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def linkedList(node):
            if not node:
                return

            l = linkedList(node.left)
            r = linkedList(node.right)

            if l and (node.right or node.left):
                r_temp = node.right
                node.right = l
                l_temp = l
                while l_temp:
                    if l_temp.right:
                        l_temp = l_temp.right
                    else:
                        break
                
                l_temp.right = r_temp
                node.left = None

            return node

            
        
        ret = linkedList(root)
        return ret

        