# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(sum, temp, flag):
            if (temp.left == None and temp.right == None) and flag == 1:
                sum += temp.val

            if temp.left:
                sum = helper(sum, temp.left, 1)

            if temp.right:
                sum = helper(sum, temp.right, 0)

            return sum

        ans = helper(0, root, 0)
        return ans