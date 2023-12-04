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
        if not root:
            return
        
        # case 2: either A or B is the root of the tree or the same subtree, we will just return the root
        if root == A or root == B:
            return root

        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        # case 1
        if left and right:
            return root

        # at this point, left and right can't be both non-null since we checked above
        # case 4 and 5, report target node or LCA back to parent
        if left:
            return left
        if right:
            return right

        # case 3, not found return null
        return None
