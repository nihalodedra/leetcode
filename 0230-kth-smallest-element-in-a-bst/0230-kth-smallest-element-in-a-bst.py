# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count = [k]
        ans = [0]

        def dfsss(node):
            if not node:
                return
            dfsss(node.left)
            if count[0] == 1:
                ans[0] =node.val
            count[0] -=1
            if count[0]>0:
                dfsss(node.right)
        dfsss(root)
        return ans[0]