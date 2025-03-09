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



