"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q --> you need to return the parent node!
    """
    def lowestCommonAncestor(self, root, p, q): # this should work for binary tree search alone, but need to debug it!
        # self.tree_traversal (root)
        # note: for binary search tree, all left node is smaller than root and right node is bigger than root.
        if root is None or root is p or root is q:
            return root

        x = root.val
        if p.val < x and q.val < x: # both p and q are in left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > x and q.val > x: #both p and q are in right subtree
            return self.lowestCommonAncestor(root.right, p, q)

        return root

    def lowestCommonAncestor_binary_tree(self, root, p, q): # this solution applies for LCA of a binary tree too
        if root is None or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left
        return right
