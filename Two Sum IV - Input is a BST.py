"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here

        if not root:
            return 

        result_pair = []
        tree_values = []

        def dfs_preorder(root: TreeNode, target: int):
            if not root:
                return
            print("node.val", root.val)
            if root.val > target:
                dfs_preorder(root.left, target)
            
            if target - root.val in tree_values:
                print("     find the pair")
                result_pair.append(root.val)
                result_pair.append(target - root.val)
                return 

            if root.val not in tree_values:
                tree_values.append(root.val)
                dfs_preorder(root.left, target)
                dfs_preorder(root.right, target)
            

        dfs_preorder(root, n)

        return result_pair[:2]
