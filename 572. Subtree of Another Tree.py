from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(s, t):
            """Helper function to check if two trees are identical"""
            if not s and not t:
                return True  # Both are None
            if not s or not t:
                return False  # One is None, the other is not
            if s.val != t.val:
                return False  # Values are different
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        def dfs(node):
            """Traverse the tree to check if subRoot exists"""
            if not node:
                return False  # Base case: Empty tree can't contain subRoot
            if isSameTree(node, subRoot):  # If we find an identical tree
                return True
            return dfs(node.left) or dfs(node.right)  # Check left and right subtrees

        return dfs(root)
        
    """ second version: 
    """
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same_tree(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False
            return (tree1.val == tree2.val and is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right))


        def dfs(root, subRoot):
            """Traverse the tree to check if subRoot exists"""
            if not root:
                return False  # Base case: Empty tree can't contain subRoot

            return is_same_tree(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)


        return dfs(root, subRoot)
