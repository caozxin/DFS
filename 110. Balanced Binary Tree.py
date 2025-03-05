# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recursion:
            #base case: if node is None
            # recursive call + what to return --> in this case, return the height

        # return value: return the height of the current tree to its parent.
        # identify states: none?
        if not root:
            #note: height of empty tree could be -1 or 0
            return True


        def dfs (node):

            if node is None:
                height = 0
                return height

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # print(left_height, right_height)
            total_height = max(left_height, right_height) + 1
            # print(node.val, left_height, right_height)
            if abs(left_height - right_height) > 1 or left_height == -1 or right_height == -1:
                print("unbalanced!")
                return -1 # only one defined return format in the recursive call! 
            return total_height  #--> this return the height of tree

        
        return True if dfs(root) != -1 else False
