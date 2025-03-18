# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # recursion:
            #base case: when input list is null
            # recursive call + what to return --> in this case, return TreeNode

        # dfs: --> construct Tree
        # identify states: pass the current state of the Tree, from parent to child
        # return value: return the Tree

#TODO: The key approach is to use the preorder array to identify the root, and the inorder array to identify the left and right subtrees.


# 1) create pre-order and in-order hashmap of {value:idx}
# 2) use pre-order list as dfs traversal order:
#     when we traversal, check if_root() using pre-order hashmap;
#     if not root, we then use in-order hashmap for left_or_right();
#     construct the tree as we go.


        if not preorder or not inorder:
            return None
        
        # Create an inorder index map for quick lookups
        in_idx = {val: idx for idx, val in enumerate(inorder)}
        
        # Define a helper function for recursion
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right or in_left > in_right:
                return None

            # Select root from preorder
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            # Find index of root in inorder traversal
            root_index = in_idx[root_val]

            # Count nodes in left subtree
            left_size = root_index - in_left

            # Recursively construct left and right subtrees
            root.left = helper(pre_left + 1, pre_left + left_size, in_left, root_index - 1)
            root.right = helper(pre_left + left_size + 1, pre_right, root_index + 1, in_right)

            return root

        # Call helper function with full range of preorder and inorder
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
