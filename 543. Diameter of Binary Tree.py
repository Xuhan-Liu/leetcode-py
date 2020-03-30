# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.maxLen = 0

    def dfs(self, node: TreeNode):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.maxLen = max(self.maxLen, left + right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.dfs(root.left) + self.dfs(root.right), self.maxLen)
