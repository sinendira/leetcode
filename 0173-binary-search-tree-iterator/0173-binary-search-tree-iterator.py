# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    res=deque()
    def __init__(self, root: Optional[TreeNode]):
        def inorder(root):
            if root:
                inorder(root.left)
                self.res.append(root.val)
                inorder(root.right)
        inorder(root)        

    def next(self) -> int:
        return self.res.popleft()

    def hasNext(self) -> bool:
        return False if  not self.res else True  


    
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()