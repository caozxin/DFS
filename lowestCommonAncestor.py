"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        """
        Case 1: if both A and B exist, return lowestCommonAncestor
        Case 2: if only A exist, return A
        Case 3: if only B exists, return B
        Case 4 if neither A nor B exists, return None
        """
        if not root:
            return
        
        # case 1: either A or B is the root of the tree or the same subtree, we will just return the root
        if root == A or root == B:
            return root
        # case 1 cont.: if both A and B exist, return lowestCommonAncestor
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        # case 1 cont.:
        if left and right:
            return root

        # at this point, left and right can't be both non-null since we checked above
        # case 2 and 3, report target node or LCA back to parent
        if left:
            return left
        if right:
            return right

        # case 4, not found return null
        return None
