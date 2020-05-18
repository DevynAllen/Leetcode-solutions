# 538. Convert BST to Greater Tree
# Runtime: 84 ms, faster than 73.55%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Total:
    value = 0

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = Total()
        self.traverseTree(root, total)
        return root
        
    def traverseTree(self, node: TreeNode, total: Total):
        if not node:
            return
        else:
            self.traverseTree(node.right, total)
            node.val+=total.value
            total.value = node.val
            self.traverseTree(node.left, total)

