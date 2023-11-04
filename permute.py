from typing import (
    List,
)

from collections import deque
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

    def permute02(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        def baktrack(nums, permutation,  res):    # Nested helper function
            if len(permutation) == len(nums):     
                res.append(permutation)            # Add current permutation to result if it uses all numbers
                return
            
            for i in range(len(nums)):

                a_num = nums.pop(0) # we want to pop the first one
                
                permutation = baktrack(nums, permutation, res)
                # permutation.append(new_solution)
                nums.append(a_num)



        res = []
        baktrack(nums, [], res)
        return res
    
    def permute03(self,nums: List[int]) -> List[List[int]]:
        def backtrack(remaining_nums, current_permutation, result):
            if not remaining_nums:
                result.append(current_permutation[:])  # Append a copy of the current permutation
                return

            for i in range(len(remaining_nums)):
                num = remaining_nums.pop(i)  # Remove the i-th element from the remaining numbers
                current_permutation.append(num) #--> make the choice
                backtrack(remaining_nums, current_permutation, result)
                current_permutation.pop()  # Remove the last element (backtrack)
                remaining_nums.insert(i, num)  # Restore the removed element with the position does not change --> undo the choice

        result = []
        backtrack(nums, [], result)
        return result

    
new_solution = Solution()
list = [1,2,3]
result = new_solution.permute03(list)
print("result", result)