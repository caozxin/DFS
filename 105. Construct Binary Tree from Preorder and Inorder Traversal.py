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

        def contruct(node, next_val):
            if not node:
                return node

            if in_idx[next_val] < in_idx[node.val]:
                node.left =  TreeNode(val =next_val)

            else:
                node.right = TreeNode(val =next_val)

            print("new node: ", node)
            # return node
            

        p_idx = {}
        in_idx = {}

        for indx, val in enumerate(preorder):
            # print(val, indx)
            p_idx[val] = indx
        print(p_idx)

        for indx, val in enumerate(inorder):
            # print(val, indx)
            in_idx[val] = indx
        print(in_idx)

        res_node = TreeNode(val =preorder[0])
        print(res_node, in_idx[res_node.val]) #everything before in_idx = 1 is left child

        for each_val in preorder[1:]:
            print(each_val)
            contruct(res_node, each_val)
            # exit()

        
