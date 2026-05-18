class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = [] 
        freq = [] 



        def backtrack(index, path): 
            if sum(path) == target: 
                res.append(path[:])
                return 
            
            if sum(path) > target or index == len(nums):
                return 
            
            # Decision 1 (include nums[index])
            path.append(nums[index])
            backtrack(index, path)

            path.pop() 

            # Decision 2 (don't include nums[index]) 
            backtrack(index + 1, path)

        backtrack(0, [])
        return res
        