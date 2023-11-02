from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output

    descriptioin: Given a set with distinct integers, return all possible subsets (in any order).

    nums = [0] 
    output = [ 
            [], 
            [0] 
            ] 

            
    nums = [1,2,3] 
    output = [ 
            [3], 
            [1], 
            [2], 
            [1,2,3], 
            [1,3], 
            [2,3], 
            [1,2], 
            [] 
            ] 
    """
    def subsets_def(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res = []
        def dfs(i, cur):
            if i == n: # when all index went over, we return 
                res.append(cur)
                return

            dfs(i + 1, cur + [nums[i]]) # this is for a binary choice to include the number in the subset at each level.
            dfs(i + 1, cur) # this is for a binary choice to NOT include the number in the subset at each level.

        dfs(0, [])

        return res
    
    def subsets_def02(nums: List[int]) -> List[List[int]]:
        def dfs(i, path):
            res.append(path[:])
            for num_idx in range(i, len(nums)):
                path.append(nums[num_idx])
                dfs(num_idx+1, path)
                path.pop()
        res = []
        dfs(0, [])
        return res
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        

        def dfs(nums, index, subset, result):
            if index == len(nums):
                
                return result
            result.append(subset[:])
            for i in range(len(nums)):
                
                end_idx = index + i+1
                curr_num = nums[i:end_idx]
                print("curr_num", curr_num)
                subset.append(curr_num)
                dfs(nums, index +1, subset, result)
                subset.pop()
                
            dfs(nums, index +1, subset, result)
            return subset


        
        def dfs02(nums, index, current_subset):
            # If we have considered all elements in 'nums', add the current subset to results.
            if index == len(nums):
                results.append(current_subset[:])
                return

            # Include the current element and recurse.
            current_subset.append(nums[index])
            dfs(nums,index + 1, current_subset)

            # Exclude the current element and recurse.
            current_subset.pop()  # Backtrack
            dfs(nums, index + 1, current_subset)

        result = list()
        if nums is not None:
            result.append([])

        if len(nums) == 1:
            result.append(nums)
            return result

        results = dfs(nums, 0, [], [])
        results.extend(result)
        return results
    



new_solution = Solution()
nums = [1,2,3]
result = new_solution.subsets_def(nums)
print("result", result)

