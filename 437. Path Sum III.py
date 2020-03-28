# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def __init__(self):
#         self.sum = 0
#         self.count = 0
#
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         self.sum = sum
#         self.start(root)
#         return self.count
#
#     def start(self, node: TreeNode):
#         if not node:
#             return
#         self.addSum(node, 0)
#         self.start(node.left)
#         self.start(node.right)
#
#     def addSum(self, node: TreeNode, pre: int):
#         if not node:
#             return
#         newSum = pre + node.val
#         if newSum == self.sum:
#             self.count += 1
#         self.addSum(node.left, newSum)
#         self.addSum(node.right, newSum)

class Solution(object):
    def pathSum(self, root, target):
        self.result = 0
        cache = {0: 1}
        # recursive to get result
        self.dfs(root, target, 0, cache)

        # return result
        return self.result


    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return
            # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        cache[currPathSum] -= 1
