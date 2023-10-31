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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        #1) tree traverse
        #2) target could round up or down. 
        #3) recursive, if smaller than left node, otherwise right node. 
        self.diff_dict = {}
        # self.diff_count = float("inf")
        self.min_diff = float("inf")
        self.min_node = None

        def dfs(self, root, target):
            if not root:
                return 0
            target = round(target)
            print(root.val, target)
            self.diff_dict[root] = abs(target - root.val)
            diff_count = abs(target - root.val)
            if diff_count <= self.min_diff:
                self.min_diff  = diff_count
                self.min_node = root
            dfs(self,root.left, target)
            dfs(self, root.right, target)

            return

            # if root.left:
            #     if root.left.val >= target:
            #         dfs(root.left, target)
            # else:
            #     dfs(root.right, target)

        dfs(self, root, target)
        print(self.diff_dict)
        print(self.min_diff, self.min_node.val)
        return self.min_node.val
