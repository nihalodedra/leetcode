# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        s = []
        r = []
        current = root
        while current is not None or len(s)>0:
            while current is not None:
                s.append(current)
                current = current.left
            current = s.pop()
            r.append(current.val)
            current = current.right
        return r