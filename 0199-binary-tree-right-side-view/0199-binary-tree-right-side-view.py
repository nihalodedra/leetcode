# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        que = deque()
        ans = []
        que.append(root)
        while len(que)!=0:
            levsize=len(que)
            for i in range(len(que)):
                node= que.popleft()
                if i == levsize-1:
                    ans.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return ans

        