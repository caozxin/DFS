from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output

    description: Given a list of numbers, return all possible permutations of it.


    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        def dfs(nums, path, used, res):    # Nested helper function
            if len(path) == len(nums):     
                res.append(path)            # Add current path to result if it uses all numbers
                return
            for i in range(len(nums)):
                if not used[i]:             # Only proceed if number hasn't been used
                    used[i] = True          
                    dfs(nums, path + [nums[i]], used, res)    # Recursive call with current number added to path
                    used[i] = False           # Reset current number to unused

        res = []
        used = [False for _ in range(len(nums))]   # Initialize used array
        dfs(nums, [], used, res)
        return res

new_solution = Solution()
list = [1,2,3]
result = new_solution.permute(list)
print("result", result)