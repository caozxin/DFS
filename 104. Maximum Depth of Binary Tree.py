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
        total = [0]

        def dfs(node, depth, path:List[int]):
            
            if node is None:
                # print("parent_val", parent_val)
                max_dep[0] = max(max_dep[0], depth) # max_dep needs to be updated here. also note that depth is local here. 
                return  # once it reaches the end, it will just retun to previous level.
            path.append(node.val)
            # Print the current traversal path
            print("path", path)
            # print("stack in curr node: ", node.val)
            if node.left:
                # print(f"Parent: {node.val}, Left Child: {node.left.val}")
                if node.val <= node.left.val:

                    # print("child is visible")
                    total[0] += 1
                    # print(f"Parent: {node.val}, Left Child: {node.left.val}")

            if node.right:
                # print(f"Parent: {node.val}, Right Child: {node.right.val}")
                if node.val <=  node.right.val:
                    # print("Parent is greater than Right Child")
                # elif node.val < node.right.val:
                #     print("Parent is smaller than Right Child")
                # else:
                    # print("child is visible")
                    total[0]  += 1
                    # print(f"Parent: {node.val}, Left Child: {node.right.val}")

            left = dfs(node.left, depth + 1, path[:]) # depth + 1 is the state here, where we want to pass the depth from parent to
            right = dfs(node.right, depth + 1, path[:]) # passing a copy of path

            # print("pop out curr node: ", node.val) # note: if the node is not parent node, it will pop right out!

        dfs(root, max_dep[0], [])

        # print("final_dep", max_dep[0])
        print('total[0] ', total[0] + 1)
        return max_dep[0]
        # return total[0] + 1
