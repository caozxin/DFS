from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countVisibleNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0  # Base case: if node is None, return 0

            # A node is visible if its value is greater than or equal to max_so_far
            visible = 1 if node.val >= max_so_far else 0
            
            # Update max_so_far to the maximum seen in the path
            max_so_far = max(max_so_far, node.val)

            # Count visible nodes in left and right subtrees
            left_visible = dfs(node.left, max_so_far)
            right_visible = dfs(node.right, max_so_far)

            return visible + left_visible + right_visible  # Sum of visible nodes

        return dfs(root, float('-inf'))  # Start DFS with negative infinity as the initial max value
