class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[] 
        

        def backtrack(index, path): 

            if index == len(nums): 
                res.append(path[:])
                return 
            
            # Decision 1 
            path.append(nums[index])
            backtrack(index + 1, path)
            


            # Decision 2 
            path.pop() 
            backtrack(index + 1, path)

        backtrack(0, [])
        return res     