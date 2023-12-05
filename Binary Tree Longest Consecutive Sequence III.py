"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
        5<6<7<>,5<>,8<>>,4<3<>,5<>,31<>>>
        1<>

"""


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    # Given in the problem, there is a k-ary tree, and we need to find the length of the longest consecutive sequence path.The path could be start and end at any node in the tree. 

    def longestConsecutive3(self, root):
        if not root:
            return 0

        def backtrack(node, current_path, length_of_path):
            length_of_path[0] = max(length_of_path[0], len(current_path))

            for child in node.children:
                if child.val == node.val + 1 or child.val == node.val - 1:
                    current_path.append(child)
                    backtrack(child, current_path, length_of_path)
                    current_path.pop()

        length_of_path = [0]  # Using a list to pass a mutable object
        backtrack(root, [root], length_of_path)

        return length_of_path[0]

    def longestConsecutive3_testing03(self, root):
        if not root:
            return 0

        def backtrack(node, current_path):
            if not node.children:
                return 1

            max_length = 1
            for child in node.children:
                if child.val == node.val + 1:
                    length = 1 + backtrack(child, current_path + 1)
                    max_length = max(max_length, length)

            return max_length

        max_length = 1
        for child in root.children:
            length = backtrack(child, 1)
            max_length = max(max_length, length)

        return max_length


    def longestConsecutive3_testing(self, root):
        if not root:
            return 0

        def backtrack(node, current_path, length_of_path):
            if not node.children:
                if node not in current_path:
                    current_path.append(node)
                    length_of_path[0] = max(length_of_path[0], len(current_path))
                return

            for child in node.children:
                if child not in current_path:
                    current_path.append(child)
                    length_of_path[0] = max(length_of_path[0], len(current_path))
                    backtrack(child, current_path, length_of_path)
                    current_path.pop()

        length_of_path = [0]
        backtrack(root, [root], length_of_path)
        return length_of_path[0]


    def longestConsecutive3_default_solution(self, root):
        
        self.longest = 0
        
        self.dfs(root)
        
        return self.longest
        
    def dfs(self, root):
        
        increasing, decreasing = 1, 1 
        
        for node in root.children:
            up, down = self.dfs(node)
            if node.val + 1 == root.val:
                increasing = max(increasing, up + 1)
            if node.val - 1 == root.val:
                decreasing = max(decreasing, down + 1)
                
        self.longest = max(self.longest, increasing + decreasing - 1)
        
        return increasing, decreasing

    def longestConsecutive3_my_solution00(self, root):
        if not root:
            return 0

        def backtrack(node, current_path, length_of_path):
            if not node.children:
                if node not in current_path:
                    current_path.append(node)
                    length_of_path[0] = max(length_of_path[0], len(current_path))
                return

            for child in node.children:
                if child not in current_path:
                    current_path.append(child)
                    length_of_path[0] = max(length_of_path[0], len(current_path))
                    backtrack(child, current_path, length_of_path)
                    current_path.pop()


        length_of_path = [0]  # Using a list to pass a mutable object
        backtrack(root, [root], length_of_path)

        return length_of_path[0]

    def longestConsecutive302(self, root):
        # Write your code here
        if not root: # None handling
            return 0
        if not root.children:
            return 1
        def backtrack(remaining_nodes, current_path, length_of_path): 
            if not root.children: # base case = goal reached
                if root not in current_path:
                    print("val")
                    print(root.val)
                    current_path.append(root)
                    length_of_path += 1
                return

            for i in range(len(remaining_nodes)):
                node = remaining_nodes.pop(i)
                if root not in current_path:
                    print("val")
                    print(root.val)
                    current_path.append(node)
                    length_of_path += 1
                    backtrack([remaining_nodes], current_path, length_of_path)
                    current_path.pop()
                    remaining_nodes.insert(i, node)
        
        length_of_path = 0
        backtrack([root], [], length_of_path)

        return length_of_path




            
