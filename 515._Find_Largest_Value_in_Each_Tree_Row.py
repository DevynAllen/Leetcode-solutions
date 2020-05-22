# 515. Find Largest Value in Each Tree Row
# Runtime: 48 ms, faster than 65.70%

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        largestValues = {}
        self.findLargestValues(0, largestValues, root)
        result = []

        for i in range(len(largestValues)):
            result.append(largestValues[i])
            
        return result
        
    def findLargestValues(self, level, largestValues, node):
        if not node:
            return
        
        if level in largestValues:
            if largestValues[level] < node.val:
                largestValues[level] = node.val
        else:
            largestValues[level] = node.val

        self.findLargestValues(level+1, largestValues, node.left)
        self.findLargestValues(level+1, largestValues, node.right)
