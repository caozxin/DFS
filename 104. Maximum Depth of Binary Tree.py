# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if the parent node <= child.node, child is visible!
        max_dep = [0] # this is a global variable and it needs to be mutal

        def dfs(node, depth):
            
            if node is None:
                max_dep[0] = max(max_dep[0], depth) # max_dep needs to be updated here. also note that depth is local here. 
                return  # once it reaches the end, it will just retun to previous level.
            
            # print("curr node: ", node.val)
            
            # max_dep[0] += 1 --> you cannot count depth here, instead, count it in child level
            # print("max_dep", max_dep[0])
            left = dfs(node.left, depth + 1) # depth + 1 is the state here, where we want to pass the depth from parent to
            right = dfs(node.right, depth + 1)

        dfs(root, max_dep[0])

        # print("final_dep", max_dep[0])
        return max_dep[0]
