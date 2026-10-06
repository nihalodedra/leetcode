# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        stack = [(root,float('-inf'))] 
        while stack:
            node,larg = stack.pop()
            if larg <= node.val:
                count += 1
            larg = max(node.val,larg)

            if node.right: stack.append((node.right,larg))
            if node.left: stack.append((node.left,larg))
        return count