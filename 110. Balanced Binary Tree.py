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
                # height = 0
                return 0

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


### update 06/10/2026:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # height-balanced: the diff between depths of two subtree from the same node <= 1
        # so this question ask to calculate the depth of any two subtree, and then count the diff
        # then how to calculate the depth of 1 subtree?
        if not root:
            return True

        def calcDepth(root, depth):
            if not root:
                return depth

            depth += 1 # we add the depth at the parent level
            # print(root.val, depth)
            return max(calcDepth(root.left, depth), calcDepth(root.right, depth)) # return the max depth between left and right subtree
            # 

        def dfs(root):
        # return calcDepth(root, 0)
            if not root:
                return True 
            # print(root, calcDepth(root, 0))
            if abs(calcDepth(root.left, 0) - calcDepth(root.right, 0)) > 1:
                print('false')
                return False
            return dfs(root.left) and dfs(root.right)

        return dfs(root)

### better approach:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # height-balanced: the diff between depths of two subtree from the same node <= 1
        # so this question ask to calculate the depth of any two subtree, and then count the diff
        # then how to calculate the depth of 1 subtree?

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            if left == -1: # if either subtree is already inbalanced, we should just immediate return -1
                return -1
            right = dfs(root.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right) # we calculate height in the child level


        return dfs(root) != -1
