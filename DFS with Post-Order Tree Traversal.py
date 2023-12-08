from typing import (
    List,
)
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
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """

    def postorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        """
        Pseudo Code: 
        None handling of root
        Set up global variables, such as result_list = []

        Def DFS Recursive calls(): 
        Base case: return if it reaches the end/bottom of the tree
        Append node.val into result_list
            Travel to node.left
            Travel to node.right
            Travel back to the root. 
        Initiate DFS Recursive call
        Return result_list 
        """

        if not root:
            return []

        result_list = []

        def dfs(curr_node: TreeNode, result_list:List[int]):
            if not curr_node:
                return
                
            if  curr_node.left == None and curr_node.right == None:
                print(curr_node.val)
                result_list.append(curr_node.val)
                return

            dfs(curr_node.left, result_list)
            dfs(curr_node.right, result_list)

        # dfs(root, result_list)
        # return result_list + [root.val]
        def dfs(curr_node: TreeNode):
            if not curr_node:
                return

            dfs(curr_node.left)
            dfs(curr_node.right)

            # Append the value after traversing left and right subtrees
            result_list.append(curr_node.val)

        dfs(root)
        return result_list


