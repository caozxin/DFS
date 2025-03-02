
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_dep = [0] # this is a global variable and it needs to be mutal

        def dfs(node, depth):
            
            if node is None:
                max_dep[0] = max(max_dep[0], depth) # max_dep needs to be updated here
                return  # once it reaches the end, it will just retun to previous level.
            
            # print("curr node: ", node.val)
            
            # max_dep[0] += 1 --> you cannot count depth here, instead, count it in child level
            # print("max_dep", max_dep[0])
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, max_dep[0])

        # print("final_dep", max_dep[0])
        return max_dep[0]
