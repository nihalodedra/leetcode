# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def solve(node):
            if not node:
                return True
            l=solve(node.left)
            if l==-1:
                return -1
            r=solve(node.right)
            if r==-1:
                return -1
            if abs(l-r)>1:
                return -1
            return 1+max(l,r)
        x=solve(root)
        if x==-1:
            return False
        else:
            return True
            