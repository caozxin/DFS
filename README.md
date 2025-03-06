![image](https://github.com/user-attachments/assets/cf0ee8ab-6e8f-4cf6-b4c6-b30307af8f7e)

<img width="591" alt="image" src="https://github.com/user-attachments/assets/08937caf-e3ea-4004-9419-fb33d3e0c739" />


<img width="644" alt="image" src="https://github.com/user-attachments/assets/e2fa56e8-a147-402d-9122-0181f054f991" />

**Backtracking and DFS are similar concepts and essentially the same thing since in DFS you always "backtrack" after exploring a deeper node. 

We have two recursive calls dfs(root.left) and dfs(root.right), and we return based on the results from the recursive calls. This is also a divide and conquer algorithm. **

![image](https://github.com/user-attachments/assets/f6e36491-3c7e-4a3b-b611-4e8acfa1ca9c)

        # recursion:
            #base case: if node is None
            # recursive call + what to return --> in this case, rreturn current subtree of its parent.

        # return value: return current subtree of its parent.
        # identify states: none?
