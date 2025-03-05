# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursion:
            #base case: if node is None
            # recursive call + what to return --> in this case, rreturn current subtree of its parent.

        # return value: return current subtree of its parent.
        # identify states: none?

        # helper invert(left_node, right_node):
            # return right_node, left_node

        # function dfs(node):
        #     if node is null:
        #         return
            
        #     left = dfs(node.left) 
        #     right = dfs(node.right)

        # in here, helper function invert left and rigth if both exist

        #     return ? --> return the inverted node from child to parent
        if not root:
            return None

        def invert_nodes(node):
            #helper function to invert left and right nodes
            if not node:
                return

            left_node = node.left
            right_node = node.right
            if not left_node and not right_node:
                return 

            if not left_node and right_node:
                
                left_node.val = right_node.val 
                right_node.val is None
            
            if not right_node and left_node:
                right_node.val = left_node.val 
                left_node.val is None

            if right_node and left_node:
                right_node.val, left_node.val = left_node.val, right_node.val
            # print(left_node)
            # print(right_node)
            print(node)
            return node

        def dfs(node):
            if not node:
                return None

            # node.left, node.right = node.right, node.left # swap it first and then traversal

            left = dfs(node.left)
            right = dfs(node.right)

            return node #or invert_nodes(right) 
        
        return dfs(root)
        # return invert_nodes(root)

        from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None  # If the tree is empty, return None
        
        def dfs(node):
            if not node:
                return None  # Base case: If the node is None, return None
            
            # Swap the left and right subtrees
            node.left, node.right = node.right, node.left
            
            # Recursively invert the left and right subtrees
            dfs(node.left)
            dfs(node.right)
            
            return node  # Return the inverted subtree

        return dfs(root)
