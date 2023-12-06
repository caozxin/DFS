from typing import (
    List,
)
from collections import deque
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    """
    def subsets_dfs(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res = []
        def dfs(i, cur):
            if i == n: # when all index went over, we return --> base case
                cur.sort()
                res.append(cur)
                return

            dfs(i + 1, cur + [nums[i]]) # this is for a binary choice to include the number in the subset at each level.
            dfs(i + 1, cur) # this is for a binary choice to NOT include the number in the subset at each level.

        dfs(0, [])

        return res

    def subsets_bfs(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        queue = [[]]
        index = 0

        while index < len(queue):
            subset = queue[index]
            index += 1
            for num in nums:
                if subset and subset[-1] >= num:
                    continue
                queue.append(subset + [num])

        return queue

    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: # None handeling
            return [[]]

        subset = []
        index = 0
        result = [] # we create a global variable here for the results. 

        def dfs_backtracking(index): # best version so far
            print("$$$index", index)
            if index >= len(nums): # this is our recursion base case
                print("***reach the base")
                result.append(subset.copy()) # we need a deep copy here, since we are modifying subsets
                return 

            #decision to include nums[index]
            print("subset to append", subset)
            subset.append(nums[index])
            dfs_backtracking(index + 1)

            #decision to not to include nums[index]:
            print("subset to pop", subset)
            subset.pop()
            dfs_backtracking(index + 1)
        

        dfs_backtracking(0) # we start with index 0 

        return result
