from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree 
    """
    def trim_b_s_t(self, root: TreeNode, minimum: int, maximum: int) -> TreeNode:
        # write your code here

        if not root:
            return None

        def trim_node(node):
            if not node:
                return None

            if node.val < minimum:
                # Node and its left subtree can be trimmed, return trimmed right subtree
                return trim_node(node.right)
            elif node.val > maximum:
                # Node and its right subtree can be trimmed, return trimmed left subtree
                return trim_node(node.left)
            else:
                # Node is within the range, continue to trim both subtrees
                node.left = trim_node(node.left)
                node.right = trim_node(node.right)
                return node

        return trim_node(root)
