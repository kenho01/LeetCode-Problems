# Thought Process:
# Post-order traversal
# Recursively swap the left and right children of each node


# Solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root
    
# Complexity Analysis:
#   Time Complexity: O(n)
#   Space Complexity:
#       For a balanced binary tree, O(log n).
#       For a skewed binary tree, the worst case is O(n).
    