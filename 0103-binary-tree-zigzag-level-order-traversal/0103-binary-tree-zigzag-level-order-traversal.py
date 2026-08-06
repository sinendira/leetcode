# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        que = deque()
        que.append(root)
        flag = True
        while que:
            n = len(que)
            level = []
            for _ in range(n):
                node = que.popleft()
                if node: level.append(node.val)
                if node and node.left: que.append(node.left)
                if node and node.right: que.append(node.right)
            if level:
                if flag:
                    ans.append(level)
                else:
                    ans.append(level[::-1])
                flag = not flag
        return ans